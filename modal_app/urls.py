from django.urls import path
from .views import HomePageView, ChangeEmailView, SignUpView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('email/<int:pk>/', ChangeEmailView.as_view(), name='change_email'),

    path('signup/', SignUpView.as_view(), name='signup'),


]
