from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
"""This assumes usage of the standard django authorization/user model
   Warning: If favorites functionality is being added to prexisting database, a database migration tool will
   be necessary to add Favorites to the database. I recommend South (http://south.aeracode.org/).
   If this is a fresh project, the standard (python manage.py syncdb) will work just fine"""

class FavoritedItem(models.Model): #Replace with name of actual item (i.e. link, video, media..)
  #Add all normal fields here, do not worry about favorites content here
     
     

#Used to extend the default user, following the django docs
class UserProfile(models.Model):
  user = models.ForeignKey(User, unique=True)
  #update first parameter here
  favorites = models.ManyToManyField(FavoritedItem, related_name='favorited_by')
     
  #Create this profile upon creation of new user
  def user_post_save(sender, instance, created, **kwargs):
    if created:
      up = UserProfile()
      up.user = instance
      up.save()
  post_save.connect(user_post_save, sender=User)
