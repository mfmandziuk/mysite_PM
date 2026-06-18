# from django.db import models

# Create your models here.


from django.db import models

class Wpis(models.Model):
    imie = models.CharField(max_length=100)
    wiadomosc = models.TextField()
    # data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.imie

class Wpis_vehicle(models.Model):
    # objects = None
    vahicle_name = models.TextField()
    vahicle_model = models.TextField()
    vahicle_rok = models.TextField(max_length=4)
    # data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vahicle_name