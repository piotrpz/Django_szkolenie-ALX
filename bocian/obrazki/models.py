from django.db import models


# Create your models here.

class Obrazek(models.Model):
    tytul = models.CharField(max_length=200)
    obrazek = models.ImageField(upload_to="uploded_images/%y/%m/%d")

    @property
    def link_do_obrazka(self):
        return self.obrazek.url

    class Meta:
        verbose_name_plural = "obrazki"
