from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):

#conviene usar el modelo que ya esta hecho y ponerle el follow
  user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

  #si es many to many se puede ver de los dos lados (a quien sigo y quien me sigue)
  follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
  
#cada vez que se cree un user, se crea un usuario
User.Usuario = property(lambda u: Usuario.objects.get_or_create(user=u)[0])