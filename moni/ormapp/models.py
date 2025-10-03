from django.db import models
from django.contrib import admin
class  Car_Inventory(models.Model):
    Plate_No = models.CharField(max_length=20, primary_key=True)
    Car_Manufacturer = models.CharField(max_length=15)
    Car_Model = models.CharField(max_length=100)
    Car_Color = models.CharField(max_length=20)
    Mileage = models.IntegerField( )

class Car_InventoryAdmin(admin.ModelAdmin):
    	list_display = ('Plate_No', 'Car_Manufacturer','Car_Model', 'Car_Color','Mileage')