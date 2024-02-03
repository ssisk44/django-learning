from django.contrib import admin
from .models import Customer

# import_export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field


class CustomerResource(resources.ModelResource):
    additional_info = Field()
    books = Field()
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'username', 'additional_info', 'rating', 'books', 'book_count')
        export_order = ('id', 'first_name', 'last_name', 'username', 'additional_info', 'rating', 'books', 'book_count')

    def dehydrate_additional_info(self, obj):
        if len(obj.additional_info) == 0:
            return "-"
        elif len(obj.additional_info) < 5:
            return obj.additional_info
        else:
            txt_list = obj.additional_info.split(' ')[:5]
            return ' '.join(txt_list) + "..."

    def dehydrate_books(self, obj):
        books = [x.isbn for x in obj.books.all()]
        return ", ".join(books)




class CustomerAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = CustomerResource


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
