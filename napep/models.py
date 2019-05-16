from django.db import models
from django.contrib.auth.models import AbstractUser
from .constants import *
# Create your models here.
class User(AbstractUser):
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    contact_address = models.CharField(max_length=200)
    dob = models.DateField(blank=True, null=True)
    dp = models.ImageField(upload_to='dp/')
    is_state = models.BooleanField(default=False)
    is_bir = models.BooleanField(default=False)
    is_ministry = models.BooleanField(default=False)
    is_lga = models.BooleanField(default=False)
    state_origin = models.CharField(max_length=50)
    lga_origin = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER, max_length=6)
    occupation = models.CharField(max_length=100)
    group = models.CharField(max_length=20)

    def __str__(self):
        return self.email

class Rider(models.Model):
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    oName = models.CharField(max_length=30)
    contactAddress = models.CharField(max_length=200)
    state_origin = models.CharField(max_length=30)
    lga_origin = models.CharField(max_length=30)
    gender = models.CharField(choices=GENDER, max_length=6)
    passport = models.ImageField(upload_to='passports/')
    phoneNumber = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)
    union_id_number = models.CharField(max_length=10)
    iceName = models.CharField(max_length=30)
    iceNumber = models.CharField(max_length=15)

    def __str__(self):
        return self.fName

class Group(models.Model):
    group_name = models.CharField(max_length=50)
    group_code = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    contact_mail = models.EmailField()

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

class OwnerNOK(models.Model):
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    relationship = models.CharField(choices=RELATIONSHIP, max_length=20)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=6)

class TricycleOwner(models.Model):
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    oName = models.CharField(max_length=30)
    state_origin = models.CharField(max_length=30)
    lga_origin = models.CharField(max_length=30)
    gender = models.CharField(choices=GENDER, max_length=6)
    phoneNumber = models.CharField(max_length=15)
    occupation = models.CharField(max_length=50)
    nok = models.ForeignKey(OwnerNOK, on_delete=models.CASCADE)


class Tricycle(models.Model):
    driver = models.ForeignKey(Rider, on_delete=models.CASCADE)
    plate_number = models.CharField(max_length=9)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=15, unique=True)
    maker = models.ForeignKey(Brand, on_delete=models.CASCADE)
    dealer_name = models.CharField(max_length=100)
    receipt_issuance_day = models.DateField()
    dealer_phone = models.CharField(max_length=15)
    chasis_number = models.CharField(max_length=30)
    dealer_receipt_number = models.CharField(max_length=15)
    status = models.CharField(choices=STATUS_CHOICE, max_length=30)
    engine_number = models.CharField(max_length=50)
    date_acquired = models.DateField(blank=True, null=True)
    owned_by_driver = models.ForeignKey(TricycleOwner, on_delete=models.CASCADE)

class RidersSuretyDetail(models.Model):
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    relationship = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)