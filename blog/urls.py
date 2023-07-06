from django.urls import path 
from rest_framework import routers
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('list/', post_list_view),
    path('detail/<str:pk>/', post_detail_view),
    path('create/', post_create_view),
    path('update/<str:pk>/', post_update_view),
    path('delete/<str:pk>/', post_delete_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)

