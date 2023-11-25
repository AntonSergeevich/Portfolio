from django.urls import path
from courses import views

urlpatterns = [
    path('all_courses/', views.coursesAllPage, name='all_courses'),
    path('course/<slug:post_slug>/', views.show_course, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]