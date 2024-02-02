from django.db import models
import uuid
from django_countries.fields import CountryField

# Create your models here.
class Publisher(models.Model):
    """
    Book publisher
    Managed only in django admin
    id: unique string
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    country = CountryField(blank_label='(Select a country)', default='', max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} from {self.country}"
