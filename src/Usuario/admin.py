from django.contrib import admin

# Para poder usarlo desde el admin
from .models import Usuario

admin.site.register(Usuario)