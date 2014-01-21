from django.conf.urls import patterns, url

from human_res.views import *


urlpatterns = patterns('human_res.views',

    url(r'^$', HumanResourceIndex.as_view(), name='index'),
    url(r'employee/$', EmployeeList.as_view(), name='employee-list'),
    url(r'employee/new/$', EmployeeCreate.as_view(), name='employee-create'),
    url(r'employee/(?P<pk>\d+)/$', EmployeeDetail.as_view(), name='employee-detail'),
    url(r'employee/(?P<pk>\d+)/edit/$', EmployeeUpdate.as_view(), name='employee-update'),
    url(r'employee/(?P<pk>\d+)/remove/$', EmployeeDelete.as_view(), name='employee-delete'),
    #url(r'edit/(?P<pk>\d+)/address/$', EditEmployeeAddress.as_view(), name='employee-address-edit'),

)
