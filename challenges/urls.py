
from django.urls import path
from . import views

urlpatterns = [
    path("", views.month_list, name="index"),
    path("<int:month>", views.monthly_challenge_view_int),
    path("<str:month>", views.monthly_challenge, name='monthlychallenge')
]