from django.contrib import admin
from .models import Company, Configuration, More

# Register your models here.
admin.site.register(Company)
admin.site.register(Configuration)
admin.site.register(More)