from rest_framework import serializers
from .models import (
    Datacenter, Floor, Room, Row,
    Rack, Enclosure, ServerType, Server,
    Cpu, Hdd, Ram, Raid, Net
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
        fields = default_fields + ('row',)

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


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = default_fields + (
            'rack', 'enclosure', 'server_type',
        )


class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = default_fields + ('server', 'socket',)


class HddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hdd
        fields = default_fields + (
            'server', 'typesize', 'volume',
            'connection_type', 'standard',
        )


class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ram
        fields = default_fields + (
            'server', 'volume', 'standard',
        )

class RaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raid
        fields = default_fields + (
            'server', 'connection_type',
        )

class NetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Net
        fields = default_fields + (
            'server', 'connection_type',
        )