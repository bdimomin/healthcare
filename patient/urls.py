from django.urls import path
from .views import home_view, register,logout_view, profile_edit

urlpatterns = [
    path('dashboard/',home_view,name='dashboard'),
    path('register/',register,name="register"),
    path('profile_edit/<int:pk>',profile_edit,name="profile_edit"),
    # path('login/',login_view,name="loginpage"),
    path('logout/',logout_view,name="logout"),
]
