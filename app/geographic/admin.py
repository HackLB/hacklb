from django.contrib import admin
import geographic.models

admin.site.register(geographic.models.Dataset)
admin.site.register(geographic.models.Parcel)