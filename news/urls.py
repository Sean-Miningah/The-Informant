from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name = "top_page"),
    path('comments/', views.comments, name = "comments_page"),
    path('comment/', views.write_comment, name = "comment"),
    path('dashboard/', views.dashboard, name = "dashboard"),
]