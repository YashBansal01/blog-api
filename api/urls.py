from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from knox import views as knox_views
from django.urls import path

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('profile/', views.ProfileViewSet.as_view({'get': 'list'}), name='profile'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]

urlpatterns = format_suffix_patterns(urlpatterns)