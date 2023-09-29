from django.db import models

# Create your models here.

class Vehicles(models.Model):
    vehicle_name=models.CharField(max_length=200)
    vehicle_number=models.CharField(max_length=200)
    vehicle_model=models.CharField(max_length=200,null=True)
    owner_name=models.CharField(max_length=200)
    km_runs=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.vehicle_name