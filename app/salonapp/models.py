from django.db import models

# Create your models here.

class Auto(models.Model):
    GEARBOX_CHOICES = (
        ('manual', 'manual'),
        ('automat', 'automat'),
        ('hybryd', 'hybryd')
    )
    name = models.CharField(max_length=100)
    price = models.FloatField()
    gearbox = models.CharField(choices=GEARBOX_CHOICES, max_length=255)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Auto'

