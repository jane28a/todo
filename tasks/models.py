from datetime import timedelta

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

def in_10_days():
    return timezone.now() + timedelta(days=10)

class Task(models.Model):

    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)
    done = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=in_10_days)
    priority = models.PositiveSmallIntegerField(validators=[
                                                        MinValueValidator(1),
                                                        MaxValueValidator(10)
                                                    ])

    def __str__(self):
        return self.title