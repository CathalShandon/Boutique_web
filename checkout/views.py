from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Theres nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_views': 'pk_test_51LtqTjAEmywH3arzDLDb85w2wkCjaoe3QMQNSZG7snWv2AJ1GGsAk6ogGejpt1uCMzBhd2QyA1I89RU9c4xGifXD00FzhIryh5',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
