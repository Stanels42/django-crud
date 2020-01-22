from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Album

class AlbumTests(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username='testuser',
      email='test@email.com',
      password='secret'
    )

    self.data = Album.objects.create(
      title='Ten Songs',
      artist='Name',
      tracks=10,
      year=2020,
      user=self.user,
    )

  def test_string_representation(self):
    data = Album(title='String Rep')
    self.assertEqual(str(data), data.title)

  def test_album_list(self):
    res = self.client.get(reverse('list'))

    self.assertEqual(res.status_code, 200)
    self.assertTemplateUsed(res, 'list.html')
    self.assertTemplateUsed(res, 'base.html')

  def test_update_view(self):
    res = self.client.get('/list/1/')

    self.assertEqual(res.status_code, 200)
    self.assertTemplateUsed(res, 'base.html')

  def test_create_view(self):
    res = self.client.get(reverse('add'))

    self.assertEqual(res.status_code, 200)
    self.assertTemplateUsed(res, 'add.html')
    self.assertTemplateUsed(res, 'base.html')

  def test_delete_view(self):
    res = self.client.get('/add/1/unadd/')

    self.assertEqual(res.status_code, 200)
    self.assertTemplateUsed(res, 'delete.html')
    self.assertContains(res, 'Are you sure you want to delete')
