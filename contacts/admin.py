from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'telephone', 'email', 'owner')
    search_fields = ('first_name', 'last_name')

admin.site.register(Contact, ContactAdmin)