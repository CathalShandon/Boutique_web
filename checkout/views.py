from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Theres nothing in your bag at the moment")
        return redirect(reversed('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_from': order_form,
    }

    return render(request, template, context)
