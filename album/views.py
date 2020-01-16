from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Album

class HomeView(TemplateView):
  template_name = 'home.html'


class AddAlbum(CreateView):
  template_name = 'add.html'
  model = Album
  context_object_name = 'Album'
  fields = ['title', 'artist', 'tracks', 'year']

class ViewAlbum(DeleteView):
  template_name = 'detail.html'
  model = Album
  context_object_name = 'Album'

class ListAlbums(ListView):
  template_name = 'list.html'
  model = Album
  context_object_name = 'Album'

class UpdateAlbum(UpdateView):
  template_name = 'home.html'
  model = Album
  context_object_name = 'Album'

class RemoveAlbum(DeleteView):
  template_name = 'home.html'
  model = Album
  context_object_name = 'Album'
