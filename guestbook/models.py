from django.db import models

class Wpis(models.Model):
    imie = models.CharField(max_length=100)
    wiadomosc = models.TextField()

    def __str__(self):
        return self.imie