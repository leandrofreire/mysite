from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

# Create your views here.
def index(request):
    posts = Entry.objects.all().order_by('-pub_date')
    return render(request, 'blog/index.html', {'posts': posts})
