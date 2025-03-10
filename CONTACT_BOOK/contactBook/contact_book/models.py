from django.db import models

# Create your models here.
class Contact_Information(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.Store_name