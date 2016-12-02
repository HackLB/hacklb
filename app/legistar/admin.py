from django.contrib import admin
import legistar.models

admin.site.register(legistar.models.AgendaItem)
admin.site.register(legistar.models.Body)
admin.site.register(legistar.models.Document)
admin.site.register(legistar.models.Meeting)