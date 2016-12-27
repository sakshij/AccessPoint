from django.db import models


class TimeStampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AddressAndPhone(models.Model):
	pin_code = models.IntegerField()
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=25)
	address = models.CharField(max_length=500)
    phone = ArrayField(models.IntegerField(max_length=10))
