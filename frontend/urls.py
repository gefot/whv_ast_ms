from django.conf.urls import url
from frontend import views

app_name = 'frontend'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^config_users/$', views.config_users, name='config_users'),

    url(r'^mgmt_cdr/$', views.mgmt_cdr, name='mgmt_cdr'),
    url(r'^mgmt_logs/$', views.mgmt_logs, name='mgmt_logs'),
    url(r'^mgmt_recording/$', views.mgmt_recording, name='mgmt_recording'),

    url(r'^vm_info/$', views.vm_info, name='vm_info'),
]