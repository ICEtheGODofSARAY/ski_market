from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

from django.db import models

from django.db import models


class SizeChoices(models.TextChoices):
    XTRASMALL = "XS", "Очень маленький"
    SMALL = "S", "Маленький"
    MEDIUM = "M", "Средний"
    LARGE = "L", "Большой"
    XTRALARGE = "XL", "Очень большой"
    XTRAXTRALARGE = "XXL", "Очень очень большой"
    XTRAXTRAXTRALARGE = "XXXL", "Очень очень очень большой"


class SkiCard(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField()


class SuitCard(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(
        validators=[MinValueValidator(1)],
    )
    image = models.ImageField()
    size = models.CharField(
        choices=SizeChoices.choices,
    )
