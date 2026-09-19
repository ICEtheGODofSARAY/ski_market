from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("hello_world/<int:page_id>/", views.hello_world, name="hello_world"),
    path("ski", views.skicard_list, name='ski_list'),
    path("suit", views.suitcard_list, name='suit_list'),
    path("ski/<int:card_id>/", views.skicard_details, name="ski_detail"),
    path("suit/<int:card_id>/", views.suitcard_details, name="suit_detail")

]
