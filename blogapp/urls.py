from django.urls import path
from . import views

urlpatterns=[
    # path('profile/', views.user_profile_view, name='user-profile'),
    path('posts/', views.post_list_create_view, name='post-list-create'),
    # path('posts/<int:pk>/', views.post_detail_view, name='post-detail'),

]