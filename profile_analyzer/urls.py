from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search_page, name='search'),
    path('candidate_list', views.CandidateListView.as_view(), name='candidate_list'),
    path('adduser/<str:username>', views.adduser, name='adduser'),
    path('deluser/<str:username>', views.del_candidate, name='deluser'),

]
