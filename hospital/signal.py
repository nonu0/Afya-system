from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from hospital.models import Patient,UserProfile

@receiver(post_save,sender=Patient)
def create_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save,sender=Patient)
def save_profile(sender,instance,**kwargs):
   instance.userprofile.save()