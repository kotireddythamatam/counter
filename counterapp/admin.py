from django.contrib import admin
from .models import Login
# Register your models here.
class Counteradmin(admin.ModelAdmin):
    list_display = ['Username','Password','Counter','datetime']
admin.site.register(Login,Counteradmin)
