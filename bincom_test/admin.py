from django.contrib import admin
from .models import States, PollingUnit, Party, Lga, AnnouncedPuResults, AnnouncedLgaResults, Ward
# Register your models here.

admin.site.register(States)
admin.site.register(PollingUnit)
admin.site.register(Party)
admin.site.register(Lga)
admin.site.register(Ward)
admin.site.register(AnnouncedPuResults)
admin.site.register(AnnouncedLgaResults)
