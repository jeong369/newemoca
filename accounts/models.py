from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class User(models.Model):
    # username = None
    name = models.CharField(max_length=50)
    age = models.IntegerField(
        validators=[
            MaxValueValidator(70),
            MinValueValidator(21)
        ]
    )
    gender = models.CharField(max_length=1, choices=(
        ('m', '남성'),
		('f', '여성'),
		('o', '기타'),
    ))
    is_staff = models.BooleanField(default=False)
    
    # USERNAME_FIELD = 'name'

