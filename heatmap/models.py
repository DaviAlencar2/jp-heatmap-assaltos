from django.db import models

MODEL_LOCATION_EXAMPLE = "RUA, N° - BAIRRO, CIDADE - SIGLA_ESTADO, CEP, PAIS"

class Assalto(models.Model):
    TYPES = [("a","assalto"),
             ("f","furto")
    ]


    latitude = models.CharField(max_length=255, blank=True, null=False)
    longitude = models.CharField(max_length=255, blank=True, null=False)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    location = models.TextField()
    type = models.CharField(max_length=1,blank=False, null=False, choices=TYPES, default="a")


    def __str__(self):
        return f"Assalto em: {self.location}, na data: {self.date}, às: {self.time}"
