from django.db import models

# Create your models here.
class BaseUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.username


class Admin(BaseUser):
    is_admin = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Receptionist(BaseUser):
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    

class Trip(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    trip_category = models.ForeignKey('TripCategory', on_delete=models.CASCADE)
    seat_type = models.ForeignKey('SeatType', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.from_location} to {self.to_location}'
    

class TripCategory(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class SeatType(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    

class Booking(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seller = models.ForeignKey('Receptionist', on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    passenger_phone = models.CharField(max_length=100)
    passenger_nid = models.CharField(max_length=100)
    total_seats = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.trip} - {self.user}'