from django.db import models

class Assalt(models.Model):
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"Assalto em: {self.location}, na data: {self.date} as: {self.time}"
