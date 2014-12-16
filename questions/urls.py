from django.conf.urls import patterns, url
from questions import views
from questions.views import CompanyDetailView, QuestionDetailView

urlpatterns = patterns('',
      url(r'^$', views.user_login, name='user_login'),
      url(r'^register/$', views.register, name='register'),
      url(r'^logout/$', views.user_logout, name='logout'),
      url(r'^companys/$', views.companys, name='companys'),
      url(r'^companys/(?P<pk>\d+)/$', views.CompanyDetailView.as_view()),
      url(r'^question/(?P<pk>\d+)/$', views.QuestionDetailView.as_view()),
      url(r'^companys/(?P<pk>\d+)/new/$', views.add_question, name='add_question'),
      url(r'^question/(?P<pk>\d+)/new/$', views.add_answer, name='add_answer'),
)
