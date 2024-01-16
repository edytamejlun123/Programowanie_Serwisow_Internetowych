from django.db import models
from django.contrib.auth.models import User
# dodane
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import datetime

# Create your models here.
class Visit(models.Model):
    VISIT_CHOICES = (
        ('Test Drive', 'Test Drive'),
        ('meeting', 'meeting with the consultant')
    )

    kind_of_visit = models.CharField(choices=VISIT_CHOICES)
    date = models.DateField(validators=[
        MinValueValidator(limit_value=datetime.date.today()),
        MaxValueValidator(limit_value=datetime.date.today() + datetime.timedelta(days=4))
    ])
    time = models.TimeField(validators=[
        MinValueValidator(limit_value=datetime.time(9, 0)),
        MaxValueValidator(limit_value=datetime.time(18, 0))
    ])
    opinion_user = models.TextField(default=" ")
    opinion_admin_answer = models.TextField(default=" ")

    def clean(self):
        # Dodatkowe sprawdzenie, aby upewnić się, że data to dzień roboczy (poniedziałek - piątek)
        if self.date.weekday() not in [0, 1, 2, 3, 4]:
            raise ValidationError("Visit date must be a weekday (Monday - Friday).")

    def __str__(self):
        return f'{self.kind_of_visit} ; {self.date}'

    class Meta:
        verbose_name = 'Visit'
        verbose_name_plural = 'Visits'
