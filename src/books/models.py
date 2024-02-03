import uuid

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from publishers.models import Publisher
from authors.models import Author
from rentals.choices import STATUS_CHOICES

# qrcode imports
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image


# Create your models here.
class BookTitle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True)  # slug replace " " with "-" for routing
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # Cascade: deletes model when publisher is deleted
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def books(self):
        return self.book_set.all()

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'pk': self.pk})


    def __str__(self):
        return f"Book name: {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Book(models.Model):
    title = models.ForeignKey(BookTitle, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=24, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)  # null=True accommodates emptiness
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    @property
    def status(self):
        if len(self.rental_set.all()) > 0:  # return most recent rental
            statuses = dict(STATUS_CHOICES)
            return statuses[self.rental_set.first().status]
        return False

    def save(self, *args, **kwargs):
        if not self.isbn:
            self.isbn = str(uuid.uuid4()).replace('-', '')[:24].lower()  # pretend this is ISBN #

            ### generate qr code
            qrcode_img = qrcode.make(self.isbn)
            canvas = Image.new('RGB', (qrcode_img.pixel_size, qrcode_img.pixel_size), 'white')
            canvas.paste(qrcode_img)
            # qr name from title
            fname = f'qr-code-{self.isbn}.png'
            # save png
            buffer = BytesIO()
            # convert to file
            canvas.save(buffer, 'PNG')
            self.qr_code.save(fname, File(buffer), save=False)
            canvas.close()

        # save all adaptations
        super().save(*args, **kwargs)