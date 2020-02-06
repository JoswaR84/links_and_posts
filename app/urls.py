from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('folder/new/', views.folder_new, name='folder_new'),
    #path('folder/detail/', views.folder_detail, name='folder_detail'),
    path('link/new/', views.link_new, name='link_new'),
    #path('link/detail/', views.link_detail, name='link_detail'),
    path('issue/new/', views.issue_new, name='issue_new'),
    #path('issue/detail/', views.issue_detail, name='issue_detail'),
]
