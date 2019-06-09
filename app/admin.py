from django.contrib import admin
from .models import Contact
from django.contrib.auth.models import Group

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','image','stream','video')
    list_per_page = 10 
    search_fields = ('name','email','phone','stream')
    list_filter = ('stream','date_added')


admin.site.register(Contact,ContactAdmin)

admin.site.unregister(Group)
