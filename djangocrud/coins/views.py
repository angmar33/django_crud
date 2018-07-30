from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "coins/index.html",
                  {'title': 'All Coins Price'})