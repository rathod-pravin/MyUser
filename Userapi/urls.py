from django.urls import path
from . import views
from knox import views as knox_views


urlpatterns = [
    path('', views.Index, name = 'test page'),
    path('api/register/', views.RegisterAPI.as_view(), name = 'register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/alluser/', views.UserAPIView.as_view(), name = 'all user'),
    path('api/user/search/', views.SearchUser.as_view(), name = 'search'),
]