import simplejson as json
import django_excel as excel

from django.shortcuts import render
from django.http import HttpResponse
from haystack.query import SearchQuerySet
from django.contrib import messages
from django.db import transaction

from .forms import *
from .models import *

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def find_note(request, pk, title):

    note = Note.objects.get(pk=pk, title=title)

    return render(request, 'note.html', {'note': note})


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
    suggestions = [result.title for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })

    return HttpResponse(the_data, content_type='application/json')

def import_data(request):

    if request.method == "POST":
        form = UploadFileForm(request.POST,
                            request.FILES)
        if form.is_valid():
            notes = request.FILES['file'].get_array()[1:]
            with transaction.atomic():
                for note in notes:
                    note_added = Note.objects.create(user=note[0].strip(), title=note[1].strip(), body=note[2])
                    note_added.save()
            messages.success(request, "Successfull Upload !")
            return HttpResponseRedirect('/upload-notes/')
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
        })

