from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *

def shop(request):
    name = "Andrii"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'shop/shop.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_pets = products_images.filter(product__category__id=1)
    products_images_aqua = products_images.filter(product__category__id=2)
    return render(request, 'shop/home.html', locals())