from django.contrib import admin
from .models import Area, TipoEquipo, lugar

# Register your models here.
admin.site.register(lugar)

admin.site.register(Area)

admin.site.register(TipoEquipo)

