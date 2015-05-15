from django.contrib import admin

# Register your models here.
from .models import (
    Datacenter, Floor, Room, Row,
    Rack, Enclosure, ServerType, Server,
    BaseComponent,
    Cpu, Hdd, Ram, Raid, Net
)


admin.site.register(Datacenter)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Row)
admin.site.register(Rack)
admin.site.register(Enclosure)
admin.site.register(ServerType)
admin.site.register(Server)
admin.site.register(BaseComponent)
admin.site.register(Hdd)
admin.site.register(Ram)