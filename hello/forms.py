from django import forms
from django.core.validators import FileExtensionValidator

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class UploadFileForm(forms.Form):
    file = forms.FileField(validators=[FileExtensionValidator(['xls', 'xlsx', 'ods', 'csv'], 'Incorect file extension.')])
