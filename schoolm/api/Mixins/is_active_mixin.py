from django.db import models


class IsActiveMixin(models.Model):

    is_active = models.BooleanField(default=True, help_text="Is the user account active?")

    class Meta:
        abstract = True

    def activate(self):
        """ Activate the user account. """
        self.is_active = True
        self.save()

    def deactivate(self):
        """ Deactivate the user account. """
        self.is_active = False
        self.save()
