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
        ('P_VAN', 'Panel Van'),
        ('C_VAN_REFIT', 'Campervan Refit'),
        ('SPEC_VEH', 'Special Vehicle')
    ]
    TRANSMISSION_TYPES = [
        ('MT', 'Manual'),
        ('AT', 'Automatic')
    ]
    GAS_CHOICES = [
        ('GAS_SAFE_CERT', 'Gas Safe Certificate'),
        ('NA', 'None'),
        ('NO_GAS', 'Gas Free')
    ]
    # Basic Info
    user = models.ForeignKey('profiles.UserProfile', default='', null=True, blank=True, on_delete=models.CASCADE)
    listing_title = models.CharField(max_length=254, default='')
    location = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    phone_number = models.IntegerField()
    name = models.CharField(max_length=254)

    # Vehicle Info
    vehicle_make_and_model = models.CharField(max_length=254)
    year = models.IntegerField()
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    transmission_type = models.CharField(
        max_length=254, choices=TRANSMISSION_TYPES)
    vehicle_length = models.IntegerField()
    vehicle_width = models.IntegerField()
    vehicle_height = models.IntegerField()
    belted_seats = models.IntegerField()
    vehicle_description = models.TextField()

    # Conversion Info
    berths = models.IntegerField()
    beds_description = models.TextField()
    gas_sign_off = models.CharField(
        max_length=254, choices=GAS_CHOICES,
        blank=True, default=GAS_CHOICES[1][1])
    max_weight = models.IntegerField()
    unladen_weight_verified = models.BooleanField(default=False, blank=True)
    unladen_weight = models.IntegerField(blank=True, null=True)
    electrics = models.ManyToManyField(Electric)
    registered_vehicle_type = models.CharField(
        max_length=254, choices=VEHICLE_TYPES)
    conversion_description = models.TextField()
    main_image = models.ImageField(
        null=True, blank=True)

    # Field which defines if the listing is active on the site, default set to 'False', awaiting admin approval.
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.listing_title


class PostImage(models.Model):
    conversion = models.ForeignKey(
        CamperConversion, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.conversion.listing_title
