from django.urls import path
from tweets import views

urlpatterns = [
    path('',views.tweet_view,name='skill'),
    path('profile/',views.profile_view,name='profile'),
    path('profile/view/',views.edit_profile_view,name='edit_profile'),
    path('post/',views.create_new_post,name='skill_post'),
    # path('profile/edit/',views.edit_profile_view,name='edit_profile'),
]