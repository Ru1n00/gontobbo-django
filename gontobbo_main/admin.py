from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Admin)
admin.site.register(models.Receptionist)
admin.site.register(models.Trip)
admin.site.register(models.TripCategory)
admin.site.register(models.SeatType)
admin.site.register(models.Booking)