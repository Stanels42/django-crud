from django.urls import path
from .views import HomeView, AddAlbum, ListAlbums, UpdateAlbum, RemoveAlbum, ViewAlbum

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('list/', ListAlbums.as_view(), name='list'),
  path('list/<int:pk>/', ViewAlbum.as_view(), name='detail'),
  path('add/', AddAlbum.as_view(), name='add'),
  path('add/<int:pk>/', UpdateAlbum.as_view(), name='update'),
  path('add/<int:pk>/unadd/', RemoveAlbum.as_view(), name='remove'),
]
