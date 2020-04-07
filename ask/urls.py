from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tags/', views.tag_list, name='tags'),
    path('tag/<str:slug>', views.tag_detail, name='tag_detail'),
    path('question/<str:slug>', views.question_detail, name='question_detail'),
    path('ask/',views.create, name="create"),
    path('signup/', views.signup_view, name = "signup"),
    path('login/', views.login_view, name = "logn"),
    path('logout/', views.logout_view, name = "logout"),
    path('hot/', views.hot_questions, name='hot_questions'),
]