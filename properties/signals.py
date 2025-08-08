from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Property
from .utils import get_all_properties

@receiver(post_save, sender=Property)
def new_property(sender, instance, **kwargs):
        cache.delete('all_properties')

@receiver(post_delete, sender=Property)
def delete_property(sender, instance, **kwargs):
        cache.delete('all_properties')