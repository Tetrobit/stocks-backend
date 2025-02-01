from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auth", views.auth, name="auth"),
    path("auth/check", views.check_auth, name="auth.check"),
    path("auth/logout", views.logout, name="auth.logout"),
    path("cbr/daily", views.daily_course, name="cbr.daily"),
    path("cbr/dynamic", views.dynamic_course, name="cbr.dynamic"),
]
