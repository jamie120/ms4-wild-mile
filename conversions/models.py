from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Electric(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class CamperConversion(models.Model):
    VEHICLE_TYPES = [
        ('P_VAN', 'Panel Van'), ('C_VAN_REFIT', 'Campervan Refit'), ('SPEC_VEH', 'Special Vehicle')
    ]
    TRANSMISSION_TYPES = [
        ('MT', 'Manual'), ('AT', 'Automatic')
    ]
    name = models.CharField(max_length=254)
    vehicle_description = models.TextField()
    conversion_description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    registered_vehicle_type = models.CharField(
        max_length=254, choices=VEHICLE_TYPES)
    transmission_type = models.CharField(
        max_length=254, choices=TRANSMISSION_TYPES)
    vehicle_length = models.IntegerField()
    berths = models.IntegerField()
    belted_seats = models.IntegerField()
    max_weight = models.IntegerField()
    unladen_weight_verified = models.BooleanField(default=False, blank=True)
    unladen_weight = models.IntegerField(blank=True, null=True)
    electrics = models.ManyToManyField(Electric)
    main_image_url = models.URLField(max_length=1024, null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ConversionImage(models.Model):
    conversion = models.ForeignKey(
        CamperConversion, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.conversion.name
