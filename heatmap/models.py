from django.db import models

class Assalto(models.Model):
    latitude = models.CharField(max_length=255, blank=True, null=False)
    longitude = models.CharField(max_length=255, blank=True, null=False)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    location = models.TextField()

    def __str__(self):
        return f"Assalto em: {self.location}, na data: {self.date}, às: {self.time}"
