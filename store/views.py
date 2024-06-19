from django.shortcuts import render


def home(req):
    context = {}
    return render(req, "store/home.html", context)