from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.blogPage, name='blog'),
    path('blog/<str:pk>/', views.postPage, name='post'),
]