from django.urls import path
from test_01 import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('crispy/', views.crispy_signup, name='crispy_signup')
]
