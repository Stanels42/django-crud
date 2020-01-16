from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Album

class HomeView(TemplateView):
  template_name = 'home.html'


class AddAlbum(CreateView):
  template_name = 'home.html'
  model = Album

class ListAlbums(ListView):
  template_name = 'home.html'
  model = Album

class UpdateAlbum(UpdateView):
  template_name = 'home.html'
  model = Album

class RemoveAlbum(DeleteView):
  template_name = 'home.html'
  model = Album
