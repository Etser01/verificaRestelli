from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class newsGiornalistiModels(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class newsArticoliModels(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    autore = models.ForeignKey(newsGiornalistiModels, on_delete=models.CASCADE, related_name="post")

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        #return reverse("PostDetailView", kwargs={"pk": self.pk})
        return f"/news/leggi-articolo/{self.id}"



