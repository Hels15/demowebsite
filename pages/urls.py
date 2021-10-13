from pages.views import HomeView, AboutView, ContactView

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view()),
    path('contact/', ContactView.as_view()),
    path('about/', AboutView.as_view()),

]