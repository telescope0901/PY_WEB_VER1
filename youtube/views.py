from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from youtube.models import Youtube
# Create your views here.
# bookmark_list.html object_list
class YoutubeLV(ListView):
    model = Youtube

class YoutubeDV(DetailView):
    model = Youtube

