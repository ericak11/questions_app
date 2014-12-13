from django.conf.urls import patterns, url
from questions import views
from questions.views import CompanyDetailView

urlpatterns = patterns('',
      url(r'^$', views.user_login, name='user_login'),
      url(r'^register/$', views.register, name='register'),
      url(r'^logout/$', views.user_logout, name='logout'),
      url(r'^companys/$', views.companys, name='companys'),
      url(r'^companys/(?P<pk>\d+)/$', views.CompanyDetailView.as_view()),
)
