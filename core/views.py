from django.shortcuts import render
from itertools import chain

from .serializers import (
    DataCenterSerializer, FloorSerializer, RoomSerializer,
    RowSerializer, RackSerializer, EnclosureSerializer,
    ServerTypeSerializer, ServerSerializer, CpuSerializer,
    HddSerializer, RamSerializer, RaidSerializer, NetSerializer,
    BaseComponentSerializer

)

from .models import (
    Datacenter, Floor, Room, Row,
    Rack, Enclosure, ServerType, Server,
    BaseComponent, Cpu, Hdd, Ram, Raid, Net
)

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route


class DataCenterViewSet(viewsets.ModelViewSet):
    queryset = Datacenter.objects.all()
    serializer_class = DataCenterSerializer
    @detail_route(methods=['GET'])
    def servers(self, request, pk):
        '''
        по урлу /datacenters/<pk>/servers выдать список серверов
        сделать два запроса - по тем, кто в стойке, и по тем, кто в корзине
        '''
        dc = self.get_object()
        in_rack = Server.objects.filter(rack__row__room__floor__datacenter=dc).all()
        in_enclosure = Server.objects.filter(enclosure__rack__row__room__floor__datacenter=dc).all()
        both = list(chain(in_rack, in_enclosure))
        serialized = ServerSerializer(both, many=True)
        return Response(serialized.data)

class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RowViewSet(viewsets.ModelViewSet):
    queryset = Row.objects.all()
    serializer_class = RowSerializer
    
class RackViewSet(viewsets.ModelViewSet):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer

    @list_route(methods=['GET'])
    def with_available_units(self, request):
        items = (
            rack for rack in self.get_queryset()
            if rack.available_units != 0
        )
        serialized = self.get_serializer(items, many=True)
        return Response(serialized.data)
    
class EnclosureViewSet(viewsets.ModelViewSet):
    queryset = Enclosure.objects.all()
    serializer_class = EnclosureSerializer

class ServerTypeViewSet(viewsets.ModelViewSet):
    queryset = ServerType.objects.all()
    serializer_class = ServerTypeSerializer

class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ViewUnusedComponentsMixin():
    '''
    выдача объектов, у которых поле server не присвоено
    '''
    @list_route(methods=['GET'])
    def unused(self, request):
        serializer = self.get_serializer_class()
        model = serializer.Meta.model
        items = model.objects.filter(server__isnull=True).all()
        serialized = serializer(items, many=True)
        return Response(serialized.data)

class BaseComponentViewSet(viewsets.ModelViewSet, ViewUnusedComponentsMixin):
    queryset = BaseComponent.objects.all()
    serializer_class = BaseComponentSerializer


class CpuViewSet(viewsets.ModelViewSet, ViewUnusedComponentsMixin):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer

class HddViewSet(viewsets.ModelViewSet, ViewUnusedComponentsMixin):
    queryset = Hdd.objects.all()
    serializer_class = HddSerializer

class RamViewSet(viewsets.ModelViewSet, ViewUnusedComponentsMixin):
    queryset = Ram.objects.all()
    serializer_class = RamSerializer

class RaidViewSet(viewsets.ModelViewSet, ViewUnusedComponentsMixin):
    queryset = Raid.objects.all()
    serializer_class = RaidSerializer

class NetViewSet(viewsets.ModelViewSet, ViewUnusedComponentsMixin):
    queryset = Net.objects.all()
    serializer_class = NetSerializer

