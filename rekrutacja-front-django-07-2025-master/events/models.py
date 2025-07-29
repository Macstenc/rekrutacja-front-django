from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.urls import reverse
from colorfield.fields import ColorField


class Event(models.Model):
    """
    Model representing an event in the system.
    """
    MODE_CHOICES = (
        ('remote', _('Remote')),
        ('in_person', _('In Person')),
    )
    
    name = models.CharField(_('Name'), max_length=200)
    description = models.TextField(_('Description'))
    start_date = models.DateTimeField(_('Start Date'))
    end_date = models.DateTimeField(_('End Date'))
    location = models.CharField(_('Location'), max_length=200)
    mode = models.CharField(_('Mode'), max_length=10, choices=MODE_CHOICES, default='in_person')
    organizer = models.CharField(_('Organizer'), max_length=200)
    color = ColorField(_('Calendar Color'), default='#003d7c')
    capacity = models.PositiveIntegerField(_('Capacity'), validators=[MinValueValidator(1)])
    registered = models.PositiveIntegerField(_('Registered Participants'), default=0)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ['start_date']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """
        Returns the URL to access a detailed record for this event.
        """
        return reverse('event_detail', args=[str(self.pk)])
        
    @property
    def is_past(self):
        """
        Check if the event is in the past.
        """
        from django.utils import timezone
        return self.end_date < timezone.now()
