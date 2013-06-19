from django.test import TestCase

from media.models import *
from django.contrib.auth.models import User
from django.test.client import Client

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class FavoritesTest(TestCase):
    def setUp(self):
        //Replace with full constructor here
        self.fav_item = FavoriteItem()
        self.fav_item.save()
        self.fav_item2 = FavoriteItem()
        self.fav_item2.save()
        self.fav_item3 = FavoriteItem()
        self.fav_item3.save()
        self.user = User(username="foo", password="bar")
        self.user.save()
        self.user2 = User(username="test", password="secret")

    def test_favorites(self):
        """
        Tests correct updating of favorites, without web interaction
        """
        self.fav_item.favorited_by.add(self.user.get_profile())
        self.assertEqual(self.user.get_profile().favorites.get(), self.fav_item)
        self.assertEqual(self.fav_item.favorited_by.get().user, self.user)
        self.fav_item2.favorited_by.add(self.user.get_profile())
        self.fav_item2.favorited_by.add(self.user2.get_profile())
        self.assertEqual(self.fav_item.favorited_by.all().first().user, self.user)
        self.assertEqual(self.fav_item.favorited_by.all().last().user, self.user2)

    def test_add(self):
        self.client = Client()
        self.client.login(username="foo",password="bar")
        #put the id of your first FavoriteItem(s) from above here
        self.client.post('/favorite/', {'id':INT})
        self.assertEqual(self.user.get_profile().favorites.get(), self.fav_item)
        
    def test_delete(self):
        self.test_add()
        #put same id from add here
        self.client.post('/delete_favorite/', {'id':INT})
        self.assertEqual(self.user.get_profile().favorites.get(), [])
        
        
