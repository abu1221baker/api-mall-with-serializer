from django.urls import path
from .views import *


urlpatterns = [
    path('profiles/', user_profile_create, name='profile-list-create'),
    path('profiles/<int:pk>/', user_profile_detail, name='profile-detail'),
    path('login/', login_view, name='login'),
]
