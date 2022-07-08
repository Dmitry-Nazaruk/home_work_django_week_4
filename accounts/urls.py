from django.urls import path, include
from accounts.views import RegisterFormView, LoginFormView, LogoutView, Create_Review

urlpatterns = [
    path('registration/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('review/', Review.as_view(), name='review'),
    path('review/', Create_Review.as_view(), name='review')

]