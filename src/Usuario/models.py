from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class MicroblProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
  follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

User.microblprofile = property(lambda u: MicroblProfile.objects.get_or_create(user=u)[0])
