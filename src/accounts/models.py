from __future__ import unicode_literals
from django.conf import settings
from django.db import models


# Create your models here.

class UserProfileManager(models.Manager):
    # use_for_related_fields = True

    def all(self):
        qs = self.get_queryset().all()
        print self.instance  # user
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile")
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="followed_by")

    # user.profile.following -- users i follow
    # user.followed_by -- users that follow me

    objects = UserProfileManager()  # UserProfile.objects.all()

    # abc = UserProfileManager()  # UserProfile.abc.all()

    def __str__(self):
        return str(self.following.all().count())

    def get_following(self):
        users = self.following.all() # User.objects.all()
        return users.exclude(username=self.user.username)
