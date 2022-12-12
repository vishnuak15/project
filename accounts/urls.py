from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    UserDetailView,
    NoteDetailView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView,
)

urlpatterns = [
    path('', views.home, name="home"),
    path('note/new/', NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='notes-detail'),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
]
