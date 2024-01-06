from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Visit(models.Model):
    VISIT_CHOICES = (
        ('Test Drive', 'Test Drive'),
        ('meeting', 'meeting with the consultant')
    )

    kind_of_visit = models.CharField(choices=VISIT_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    opinion_user = models.TextField(default=" ")
    opinion_admin_answer = models.TextField(default=" ")

    def __str__(self):
        return f'{self.kind_of_visit} ; {self.date}'

    class Meta:
        verbose_name = 'Visit'
        verbose_name_plural = 'Visits'
