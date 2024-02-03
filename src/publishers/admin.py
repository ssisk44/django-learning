from django.contrib import admin
from .models import Publisher
# import-export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

class PublisherResource(resources.ModelResource):
    date = Field()
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'country', 'date', 'created')
        export_order = ('id', 'name', 'country', 'date', 'created')

    def dehydrate_date(self, obj):
        return obj.created.strftime('%d/%m/%y')




class PublisherAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PublisherResource

# Register your models here.
admin.site.register(Publisher, PublisherAdmin)