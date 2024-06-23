from django.shortcuts import render, redirect
import faker
from customers.models import Customer
from store.models import Store
from products.models import Product
from orders.models import Order, OrderItem


def home(req):
    context = {}
    return render(req, "store/home.html", context)

def newday(req):
    # generate random customers
    # generate random orders from products in stock
    return redirect("store:home")

def settings(req):
    context = {}
    return render(req, "store/settings.html", context)