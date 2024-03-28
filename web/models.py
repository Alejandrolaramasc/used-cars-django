from django.db import models
import uuid

# Create your models here.
class Cars(models.Model):
    car_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    year = models.IntegerField()
    seat_number = models.IntegerField()
    color = models.CharField(max_length=15)
    brand = models.CharField(max_length=15)
    trans_type = models.CharField(max_length=15)
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    odometer = models.IntegerField()
    price = models.IntegerField()

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

