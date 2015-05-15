from django.contrib import admin

# Register your models here.
from .models import Datacenter, Floor, Cpu

admin.site.register(Datacenter)
admin.site.register(Floor)
admin.site.register(Cpu)