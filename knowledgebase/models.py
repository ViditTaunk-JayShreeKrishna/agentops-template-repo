from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FAQ(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f"{self.city.name} - {self.question}"

class BookingDetail(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city.name} Booking Info"