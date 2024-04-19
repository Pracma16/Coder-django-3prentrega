from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Avatar


@receiver(models.signals.post_save, sender=User)
def crear_avatar_predeterminado(sender, instance, created, **kwargs):
    if created:
        avatar_predeterminado = Avatar(user=instance)
        avatar_predeterminado.save()
        

        