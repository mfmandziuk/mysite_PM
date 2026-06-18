# from django.db import models

# Create your models here.


from django.db import models

class Wpis(models.Model):
    imie = models.CharField(max_length=100)
    wiadomosc = models.TextField()
    # data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.imie