from django.contrib import admin

from .models.user import User
from .models.paciente import Paciente

admin.site.register(User)
admin.site.register(Paciente)

# Register your models here.
