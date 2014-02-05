from django.conf.urls import patterns, url
from TGTapp import views

#makes the base index for TGTapp
urlpatterns = patterns('',
        url(r'^$', views.index, name='index')
)