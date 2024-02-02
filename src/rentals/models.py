from django.db import models
from books.models import Book
from customers.models import Customer
from datetime import timedelta

# Create your models here.
STATUS_CHOICES = (
    ('#0', 'rented'),
    ('#1', 'returned'),
    ('#2', 'lost'),
    ('#3', 'delayed'),
)

class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    rent_start_date = models.DateField(help_text='Book rental date')
    rent_end_date = models.DateField(help_text='Book due date', blank=True)
    return_date = models.DateField(help_text='Book return date', blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.book.isbn} rented by {self.customer.username}'

    def save(self, *args, **kwargs):
        if not self.rent_end_date:
            self.rent_end_date = self.rent_start_date + timedelta(days=14)
        super().save(*args, **kwargs)
