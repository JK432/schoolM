from django.db import models
from django.utils import timezone


class SoftDeleteMixin(models.Model):
    """ A mixin for adding soft deletion functionality to a model."""

    is_deleted = models.BooleanField(default=False, db_index=True, help_text="Is the record deleted?")
    deleted_at = models.DateTimeField(null=True, blank=True, help_text="Date and time of deletion")

    class Meta:
        abstract = True

    def delete(self):
        """ Soft delete the record."""
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def undelete(self):
        """ Restore a soft-deleted record."""
        self.is_deleted = False
        self.deleted_at = None
        self.save()
