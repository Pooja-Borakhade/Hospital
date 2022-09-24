from django.contrib import admin

from .models import *
# Register your models here.       #,Owner,Department,Doctor

admin.site.register([Hospital,Owner,Department,Doctor])