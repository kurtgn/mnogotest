from rest_framework import serializers
from .models import (
    Datacenter, Floor, Room, Row,
    Rack, Enclosure, ServerType, Server,
    BaseComponent, Cpu, Hdd, Ram, Raid, Net
)

default_fields = ('pk', 'name',)

class DataCenterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Datacenter
        fields = default_fields + ('address',)



class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = default_fields + ('datacenter',)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = default_fields + ('floor',)

class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = default_fields + ('room',)

class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = default_fields + ('row', 'available_units',)

class EnclosureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enclosure
        fields = default_fields + ('rack',)

class ServerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerType
        fields = default_fields + (
            'cpu_slots', 'cpu_socket', 'ram_slots',
            'ram_standard', 'hdd_slots', 'hdd_typesize',
            'hdd_standard',
        )

base_component_fields = (
    'manufacturer', 'model', 'serial_number', 'server',
)

class BaseComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseComponent
        fields = default_fields + base_component_fields + (
            'component_type',
        )

        # сюда можно добавить не просто поле component_type,
        # а целый объект - child

class ServerSerializer(serializers.ModelSerializer):

    plugged_components = BaseComponentSerializer(many=True, read_only=True)
    class Meta:
        model = Server
        fields = default_fields + (
            'rack', 'enclosure', 'server_type', 'plugged_components',
        )

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = default_fields + base_component_fields + ('socket',)


class HddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hdd
        fields = default_fields + base_component_fields + (
            'typesize', 'volume',
            'connection_type', 'standard',
        )


class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ram
        fields = default_fields + base_component_fields + (
            'volume', 'standard',
        )

class RaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raid
        fields = default_fields + base_component_fields + (
            'connection_type',
        )

class NetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Net
        fields = default_fields + base_component_fields + (
            'connection_type',
        )


