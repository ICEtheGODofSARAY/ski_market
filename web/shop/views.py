from django.shortcuts import render
from .models import SkiCard, SuitCard


def skicard_list(request):
    qs = SkiCard.objects.all()
    context = {"ski_cards": qs}
    return render(request, "shop/ski_list.html", context)

def skicard_details(request, card_id):
    card = SkiCard.objects.get(pk=card_id)
    context = {"ski_card": card}
    return render(request, "shop/ski_detail.html", context)

def suitcard_list(request):
    qs = SuitCard.objects.all()
    context = {"suit_cards": qs}
    return render(request, "shop/suit_list.html", context)

def suitcard_details(request, card_id):
    card = SuitCard.objects.get(pk=card_id)
    context = {"suit_card": card}
    return render(request, "shop/suit_detail.html", context)

def home_page(request):
    return render(request, template_name="shop/home_page.html")