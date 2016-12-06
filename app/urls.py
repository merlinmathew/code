from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'', views.login2, name='login'),
    url(r'home/', views.home, name='home'),
    url(r'^login/', views.login2, name='login'),
    url(r'^logout/', views.logout2, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^edit/(?P<pk>\d+)/$', views.prof_edit, name='prof_edit'),

]
