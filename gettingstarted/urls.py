from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^search/', include('haystack.urls')),
    url(r'search/autocomplete/', hello.views.autocomplete, name='autocomplete'),
    url(r'note/(?P<pk>[0-9]+)/(?P<title>[A-Za-z\s:,0-9]+)/', hello.views.find_note, name='note'),
    url(r'^upload-notes/$', hello.views.import_data, name='import data'),
    url(r'^admin/', include(admin.site.urls)),
]
