from django.conf.urls import patterns, url
from frontendadmin.views import add, change, delete, success, success_delete, reverse_admin_url
from django.views.decorators.cache import never_cache

urlpatterns = patterns('',
                       url(r'^add/(?P<app_label>[\w]+)/(?P<model_name>[\w]+)/$',
                           never_cache(add),
                           name='frontendadmin_add'),

                       url(r'^change/(?P<app_label>[\w]+)/(?P<model_name>[\w]+)/(?P<instance_id>[\d]+)/$',
                           never_cache(change),
                           name='frontendadmin_change'),

                       url(r'^delete/(?P<app_label>[\w]+)/(?P<model_name>[\w]+)/(?P<instance_id>[\d]+)/$',
                           never_cache(delete),
                           name='frontendadmin_delete'),

                       url(r'^success/$',
                           success,
                           name='frontendadmin_success'),

                       url(r'^success_delete/$',
                           success_delete,
                           name='frontendadmin_success_delete'),

                       url(r'^reverse_admin_url/(?P<app_label>[\w]+)/(?P<model_name>[\w]+)/(?P<instance_id>[\d]+)/(?P<action>[\w]+)$',
                       #url(r'^reverse_admin_url/(?P<app_label>[\w]+)/$',
                           reverse_admin_url,
                           name='frontendadmin_reverse_admin_url'),
)
