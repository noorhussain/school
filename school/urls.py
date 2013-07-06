from django.conf.urls import patterns, include, url
from students import views
from teachers import views
from teachers.views import *
from students.views import *
from staff import views
from staff.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', school.as_view(), name='school'),
    url(r'students', Details.as_view(), name='details'),
    url(r'^shows/(?P<id>\w+)/$', Shows.as_view(),name='shows'),
    url(r'^deletes/(?P<id>\w+)/$', Deletes.as_view(),name='Deletes'),
    url(r'^adds/$', Adds.as_view(),name='adds'),
    url(r'^errors/$', Errors.as_view(),name='errors'),
    url(r'teachers', Detail.as_view(), name='detail'),
    url(r'^show/(?P<id>\w+)/$', Show.as_view(),name='show'),
    url(r'^delete/(?P<id>\w+)/$', Delete.as_view(),name='Delete'),
    url(r'^add/$', Add.as_view(),name='add'),
    url(r'^error/$', Error.as_view(),name='error'),
    url(r'staff', Detailst.as_view(), name='detail'),
    url(r'^showst/(?P<id>\w+)/$', Showst.as_view(),name='shows'),
    url(r'^deletest/(?P<id>\w+)/$', Deletest.as_view(),name='Deletes'),
    url(r'^addst/$', Addst.as_view(),name='adds'),
    url(r'^errorst/$', Errorst.as_view(),name='errors'),
    url(r'fee', Detailst.as_view(), name='detail'),   
)
