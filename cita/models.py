from django.db import models

# Create your models here.
from psicologo.models import Psicologo

class Cita(models.Model):
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE, default=None)
    dateTime = models.DateTimeField(auto_now=False, auto_now_add=False)
    plataforma = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.dateTime, self.plataforma)