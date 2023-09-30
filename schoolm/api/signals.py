from django.db.models.signals import pre_delete
from django.dispatch import receiver
# from .models import Teacher

# @receiver(pre_delete, sender=Teacher)
# def delete_user_on_teacher_delete(sender, instance, **kwargs):
#     # Check if the teacher has an associated user
#     if instance.user:
#         instance.user.delete()