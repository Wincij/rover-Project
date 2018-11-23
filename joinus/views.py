# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def joinus(request):
    urldict = {"active":"joinus"}
    return render(request, 'joinus/joinus.html', urldict)
