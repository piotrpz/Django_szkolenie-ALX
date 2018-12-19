from django.db import models

# Create your models here.
from blog.models import Wpis


class Komentarze(models.Model):
    tresc = models.TextField()
    nickname = models.CharField(max_length=200, unique=True)
    tytul = models.CharField(max_length=200)
    email = models.EmailField()
    data = models.DateTimeField(auto_now_add=True)
    wpis = models.ForeignKey(Wpis, on_delete=models.CASCADE)

    def __str__(self):
        return f"Komentarz: {self.nickname} | {self.data} | {self.tytul}"

    class Meta:
        verbose_name_plural = "Komentarze"

