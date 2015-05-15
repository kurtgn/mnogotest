from django.shortcuts import render

from .serializers import (
    DataCenterSerializer, FloorSerializer, RoomSerializer,
    RowSerializer, RackSerializer, EnclosureSerializer,
    ServerTypeSerializer, ServerSerializer, CpuSerializer,
    HddSerializer, RamSerializer, RaidSerializer, NetSerializer

)

from .models import (
    Datacenter, Floor, Room, Row,
    Rack, Enclosure, ServerType, Server,
    Cpu, Hdd, Ram, Raid, Net
)

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route


class DataCenterViewSet(viewsets.ModelViewSet):
    queryset = Datacenter.objects.all()
    serializer_class = DataCenterSerializer

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

