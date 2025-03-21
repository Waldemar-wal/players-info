from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser



class Race(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EquipmentType(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class Player(AbstractUser):
    level = models.IntegerField(default=1)
    power = models.IntegerField(default=0)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "player"
        verbose_name_plural = "players"

    def __str__(self):
        return (f"Player: {self.username}, "
                f"level: {self.level}, power: {self.power}")


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    player = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="equipments",
        blank=True
    )

    def __str__(self):
        return f"{self.name}: {self.description}"




