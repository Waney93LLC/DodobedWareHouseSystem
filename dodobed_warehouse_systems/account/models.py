from django.db import models


class User(auth_models.AbstractBaseUser,auth_models.PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Address(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    street2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    delivery_instructions = models.TextField(blank=True)

    def __str__(self):
        return self.name