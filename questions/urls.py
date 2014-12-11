# from django.shortcuts import get_object_or_404, render_to_response
# from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
# from django.template import RequestContext
# from questions.models import Question, Answer, Company

# urlpatterns = patterns('',
#   url(r'^$', views.BookList.as_view(), name='book_list'),
#   url(r'^new$', views.BookCreate.as_view(), name='book_new'),
#   url(r'^edit/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_edit'),
#   url(r'^delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
# )

# from django.conf.urls import url

# from . import views

# urlpatterns = [
#     url(r'^articles/2003/$', views.special_case_2003),
#     url(r'^articles/([0-9]{4})/$', views.year_archive),
#     url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
#     url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
# ]

from django.conf.urls import patterns, url
from questions import views

urlpatterns = patterns('',
      url(r'^$', views.index, name='index')
)
