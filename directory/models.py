from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from utility.behaviours import TimeStampable, AddressAndPhone


class Dealer(TimeStampable, AddressAndPhone, models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    owner = models.OneToOneField(User)
    intercom = ArrayField(models.IntegerField(max_length=10)) #TODO: Check intercom numbers max length

    class Meta:
        verbose_name_plural = 'dealers'
        verbose_name        = 'delaer'

    def __str__(self):
        return str(self.id)


class Brand(TimeStampable, models.Model):
	name = models.CharField(max_length=100)


class Product(TimeStampable, models.Model):
	name = models.CharField(max_length=100)
	brand = models.OneToOneField(Brand)


class Service(TimeStampable, models.Model):
	name = models.CharField(max_length=100)


class OldProduct(TimeStampable, models.Model):
	name = models.CharField(max_length=100)
	# product_category = models.CharField() TODO: What are these categories?


class ServiceCentre(TimeStampable, AddressAndPhone, models.Model):
	name = models.CharField(max_length=100)


class ProductServiceCentre(TimeStampable, models.Model):
	service_centre = models.OneToOneField(ServiceCentre)
	product = models.OneToOneField(Product)


class ProductDealer(TimeStampable, models.Model):
	product = models.OneToOneField(Product)
	dealer = models.OneToOneField(Dealer)


class ServiceDealer(TimeStampable, models.Model):
	service = models.OneToOneField(Service)
	dealer = models.OneToOneField(Dealer)


class OldProductDealer(TimeStampable, models.Model):
	product = models.OneToOneField(OldProduct)
	dealer = models.OneToOneField(Dealer)


class PriceList(TimeStampable, models.Model):
	product = models.OneToOneField(Product)
	prices = models.URLField()


class Vendor(TimeStampable, models.Model):
	name = models.CharField(max_length=100)
	product = models.OneToOneField(Product)


class Distributor(TimeStampable, models.Model):
	name = models.CharField(max_length=100)
	product = models.OneToOneField(Product)


class ContactPerson(TimeStampable, models.Model):
	name = models.CharField()
	area = models.CharField()
	user = models.OneToOneField(user)
	phone = ArrayField(models.IntegerField(max_length=10))
	vendor = models.ForiegnKey(Vendor, related_name='contact_people', blank=True, null=True)
	distributor = models.ForiegnKey(Distributor, related_name='contact_people', blank=True, null=True)


class NewProduct(TimeStampable, models.Model):
	product = models.OneToOneField(Product)
	details = models.URLField()


class Event(TimeStampable, AddressAndPhone, models.Model):
	name = models.CharField
	start_datetime = models.DateTimeField()
	end_datetime = models.DateTimeField()
	organizer = models.CharField() #TODO: Should this be mapped to user?
