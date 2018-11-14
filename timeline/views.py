from django.shortcuts import render
from .models import Entry

def timeline(request):
    entries = Entry.objects
    return render(request, 'timeline/timeline.html', {'entry':entries})
