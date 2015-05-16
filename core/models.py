from django.db import models
from model_utils.managers import InheritanceManager

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
    @property
    def servers(self):
        return Server.objects.filter(rack__row__room__floor__datacenter=self).all()


class Floor(BaseModel):
    datacenter = models.ForeignKey(Datacenter)


class Room(BaseModel):
    floor = models.ForeignKey(Floor)


class Row(BaseModel):
    room = models.ForeignKey(Room)


class Rack(BaseModel):
    row = models.ForeignKey(Row)
    unit_capacity = models.IntegerField(default=47)

    @property
    def available_units(self):
        '''
        агрегируем корзины и сервера в этой стойке по высоте.
        если объектов в стойке нет, то aggregate выдает None
        и мы вместо None ставим 0.

        в self.server_set.all() не войдут сервера, лежащие в корзинах,
        если при постановке сервера в стойку запретить присваивать серверу
        сразу оба FK: и FK стойки, и корзины
        '''
        sum_enclosure_height = self.enclosure_set.aggregate(models.Sum('units_height'))['units_height__sum']
        if sum_enclosure_height is None:
            sum_enclosure_height = 0
        sum_single_servers_height = self.server_set.aggregate(models.Sum('units_height'))['units_height__sum']
        if sum_single_servers_height is None:
            sum_single_servers_height = 0
        used_units = sum_enclosure_height + sum_single_servers_height
        return self.unit_capacity - used_units



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
    units_height = models.IntegerField(default=1)
    server_type = models.ForeignKey(ServerType)

    @property
    def plugged_components(self):
        return self.basecomponent_set.all()

class BaseComponent(BaseModel):
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    server = models.ForeignKey(Server, null=True, blank=True)

    objects = InheritanceManager()
    '''
    менеджер, кот.позволяет доставать детей
    из родительских объектов BaseComponent
    '''

    @property
    def component_type(self):
        subclass = BaseComponent.objects.get_subclass(pk=self.pk)
        return subclass.__class__.__name__


class Cpu(BaseComponent):
    socket = models.CharField(max_length=50)
    def __setattr__(self, key, value):
        '''
        если объекту присваивается server, у которого в типе сервера
        прописан другой возможный socket, - выдать исключение

        позже это исключение можно
        красиво обернуть в json на уровне rest

        аналогично можно перехватить присвоение
        в объектах hdd, ram, raid, net
        '''
        if key == 'server' and value is not None:
            compatible_socket = value.server_type.cpu_socket
            if compatible_socket != self.socket:
                raise AttributeError('Incompatible component')

            '''
            Выбрать все компоненты сервера,
            отобрать из них только CPU
            и сравнить допустимое макс.кол-во с текущим кол-вом.
            Если текущее кол-во равно допустимому
            (и если self не входит в эти процессоры),
            выдаем ошибку.

            то же самое можно проделать в объектах hdd, ram, raid, net
            '''
            components = value.basecomponent_set.select_subclasses()
            cpus = [e for e in components if isinstance(e, Cpu)]
            if len(cpus) == value.server_type.cpu_slots and self not in cpus:
                raise AttributeError('Exceeded number of slots')
        super(Cpu, self).__setattr__(key, value)


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