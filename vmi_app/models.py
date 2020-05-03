from django.db import models

# Create your models here.

class Index(models.Model):
    vmi_index=models.DecimalField(decimal_places=2,max_digits=4)
    engineoil_index=models.DecimalField(decimal_places=2,max_digits=4)
    oilfilter_index=models.DecimalField(decimal_places=2,max_digits=4)
    sparkplug_index=models.DecimalField(decimal_places=2,max_digits=4)
    fuelfilter_index=models.DecimalField(decimal_places=2,max_digits=4)
    airfilter_index=models.DecimalField(decimal_places=2,max_digits=4)
    tyre_index=models.DecimalField(decimal_places=2,max_digits=4)
    brakefluid_index=models.DecimalField(decimal_places=2,max_digits=4)
    coolant_index=models.DecimalField(decimal_places=2,max_digits=4)
    battery_index=models.DecimalField(decimal_places=2,max_digits=3)
    """clutchplate_index=models.DecimalField(decimal_places=2,max_digits=4)
    wheelalign_index=models.DecimalField(decimal_places=2,max_digits=4)"""