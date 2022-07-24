from django.db import models
from django.core.validators import MaxValueValidator


class Client(models.Model):
   
    full_name = models.CharField(max_length=250,blank=False,null=False) 
    phone_number = models.BigIntegerField(validators=[MaxValueValidator(9999999999)],blank=False,null=False)
    seondary_no = models.BigIntegerField(validators=[MaxValueValidator(9999999999)],blank=False,null=False)
    email =  models.EmailField(max_length=40,null=False,blank=True)
    seconday_em =  models.EmailField(max_length=40,null=False,blank=False)
    address = models.TextField(blank=True,null=True)
  

    def __str__(self):
        return self.full_name + " " + self.email
