from django.urls import path

from . import views

urlpatterns = [
    path("", views.card_list, name="index"),
    path("<int:card_id>/", views.card_details, name="detail"),
]
