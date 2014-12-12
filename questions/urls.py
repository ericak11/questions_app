from django.conf.urls import patterns, url
from questions import views

urlpatterns = patterns('',
      url(r'^$', views.user_login, name='user_login'),
      url(r'^register/$', views.register, name='register'),
      url(r'^logout/$', views.user_logout, name='logout'),
)
