from django.contrib import admin
from pythontool.models import *

# Register your models here.

@admin.register(Publisher)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','county','state_province','city')
    search_fields = ('name')

admin.site.register(Author)
admin.site.register(AuthorDetail)
# admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book)

