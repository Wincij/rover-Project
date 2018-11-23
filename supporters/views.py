from django.shortcuts import render
from .models import Supporter
def supporters(request):
    supporters = Supporter.objects
    return render(request, 'supporters/supporters.html', {"supporters":supporters})
