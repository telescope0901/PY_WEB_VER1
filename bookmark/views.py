from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from bookmark.models import Bookmark
# Create your views here.
# bookmark_list.html object_list
class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

