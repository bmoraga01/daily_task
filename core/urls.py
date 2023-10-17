from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', IndexPage.as_view(), name='index_page'),
    
    path('profile', ProfileDetail.as_view(), name='profile_detail'),
    path('profile/edit', EditProfile.as_view(), name='edit_profile'),
    
]
