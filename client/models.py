from django.db import models


class Client(models.Model):
   
    full_name = models.CharField(max_length=250,blank=False,null=False) 
    phone_number = models.IntegerField(max_length=20,blank=False,null=False)
    seondary_no = models.IntegerField(max_length=20,blank=False,null=False)
    email =  models.EmailField(max_length=40,null=False,blank=True)
    seconday_em =  models.EmailField(max_length=40,null=False,blank=False)
    address = models.TextField(blank=True,null=True)
  

    def __str__(self):
        return self.full_name + " " + self.email
