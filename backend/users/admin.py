from django.contrib import admin
from .models import *
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields =('id',)

admin.site.register(Profile,ProfileAdmin)