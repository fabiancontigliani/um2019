from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
	#la publicacion si o si tiene que tener el usuario que la creo 
  user = models.ForeignKey(User, related_name='publicacion', on_delete=models.DO_NOTHING)
  body = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-created_at',)