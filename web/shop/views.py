from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

from utils.translate import translate
from .models import SkiCard

def card_list(request):
    qs = SkiCard.objects.all()
    context = {"ski_cards": qs,
               "today": translate(today_date = date.today())}
    return render(request, "shop/ski_list.html", context)

def card_details(request, card_id):
    card = SkiCard.objects.get(pk=card_id)
    context = {"ski_card": card}
    return render(request, "shop/ski_detail.html", context)