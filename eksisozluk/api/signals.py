# from django.contrib.auth.models import User
from .models import Explanation,User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



@receiver(post_save, sender=Explanation)
def increase_like_count(sender, instance, created, **kwargs):
    if created:
        user = User.objects.get(username = instance.user)
        print(user.username, user.total_likes)
        user.total_likes = user.total_likes + 1
        if user.total_likes >= 50:
            user.status = 'MD'
        elif user.total_likes >= 100:
            user.status = 'PR'
        user.save()
        print('Entry Yaratildi', instance.user)

@receiver(post_save, sender=User)
def create_token(sender, instance, created, **kwargs):

    if created:
        # user = User.objects.get(username = instance.user)
        Token.objects.create(user = instance)