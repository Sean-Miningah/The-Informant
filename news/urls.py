from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name = "top_page"),
    path('comments/', views.comments, name = "comments")
]