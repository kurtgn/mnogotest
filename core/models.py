from django.db import models

# Create your models here.



class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        abstract = True
    def __str__(self):
        return '{} {}'.format(
            self.__class__.__name__, self.name
        )


class Datacenter(BaseModel):
    address = models.CharField(max_length=100)


class Floor(BaseModel):
    datacenter = models.ForeignKey(Datacenter)


class Room(BaseModel):
    floor = models.ForeignKey(Floor)


class Row(BaseModel):
    room = models.ForeignKey(Room)


class Rack(BaseModel):
    row = models.ForeignKey(Row)
    unit_capacity = models.IntegerField(default=47)

class Enclosure(BaseModel):
    rack = models.ForeignKey(Rack, blank=True, null=True)
    units_height = models.IntegerField(default=3)


class ServerType(BaseModel):
    cpu_slots = models.IntegerField()
    cpu_socket = models.CharField(max_length=50)
    ram_slots = models.IntegerField()
    ram_standard = models.CharField(max_length=50)
    hdd_slots = models.IntegerField()
    hdd_typesize = models.CharField(max_length=50)
    hdd_standard = models.CharField(max_length=50)
    # а поле hdd_connection_type не нужно? оно есть в атрибутах модели Hdd

    # по-хорошему нужно сделать cpu_socket, ram_standard, hdd_typesize,
    # hdd_standard отдельными моделями, и связать их
    # с ServerType и комплектующимим



class Server(BaseModel):
    rack = models.ForeignKey(Rack, blank=True, null=True)
    enclosure = models.ForeignKey(Enclosure, blank=True, null=True)
    # нужно следить, чтобы невозможно было добавить сразу оба FK rack и enclosure
    server_type = models.ForeignKey(ServerType)
    # при добавлении комплектующих проверять соответствие типу и свободные слоты


class BaseComponent(BaseModel):
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    server = models.ForeignKey(Server, null=True, blank=True)

    class Meta:
        abstract = True



class Cpu(BaseComponent):
    socket = models.CharField(max_length=50)


class Hdd(BaseComponent):
    typesize = models.CharField(max_length=50)
    volume = models.IntegerField() # нужно где-нибудь зафиксировать единицу измерения
    connection_type = models.CharField(max_length=50)
    standard = models.CharField(max_length=10, choices=(
        ('HDD', 'HDD'),
        ('SSD', 'SSD'),
        ('Hybrid', 'Hybrid')
    ))

class Ram(BaseComponent):
    volume = models.IntegerField() # нужно где-нибудь зафиксировать единицу измерения
    standard = models.CharField(max_length=50)

class Raid(BaseComponent):
    connection_type = models.CharField(max_length=50)

class Net(BaseComponent):
    connection_type = models.CharField(max_length=50)