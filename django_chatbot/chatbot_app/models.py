from datetime import datetime
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class Chatbot(models.Model):
    qus = models.CharField(
        max_length=1000,
        verbose_name="Question"
        )
    ans = models.TextField(
        verbose_name='Answer'
        )
    timestamp = models.DateTimeField(
        blank=True,
        auto_now=True
        )

    def __str__(self):
        return f'{self.qus}'


    class Meta:
        verbose_name='Chatbot'