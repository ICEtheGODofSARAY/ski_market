from django.urls import path

from . import views

urlpatterns = [
    path("ski", views.skicard_list),
    path("suit", views.suitcard_list),
    path("ski/<int:card_id>/", views.skicard_details, name="ski_detail"),
    path("suit/<int:card_id>/", views.suitcard_details, name="suit_detail"),
]
