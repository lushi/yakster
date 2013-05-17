from django.db import models
from django.contrib.auth.models import User
import hashlib
class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
      return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])