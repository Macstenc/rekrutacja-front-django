from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import datetime
from calendar import monthrange
import calendar
from django.views.generic import DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm


def index(request):
    """
    Home page view showing the next 5 upcoming events.
    """
    upcoming_events = Event.objects.filter(
        start_date__gte=timezone.now()
    ).order_by('start_date')[:5]
    
    return render(request, 'events/index.html', {
        'upcoming_events': upcoming_events,
    })


class EventDetailView(DetailView):
    """
    View for displaying event details.
    """
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'


class EventCreateView(CreateView):
    """
    View for creating a new event.
    """
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create Event')
        return context
    
    def form_valid(self, form):
        messages.success(self.request, _('Event created successfully!'))
        return super().form_valid(form)


class EventUpdateView(UpdateView):
    """
    View for updating an existing event.
    """
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Edit Event')
        return context
    
    def get_success_url(self):
        return reverse_lazy('event_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, _('Event updated successfully!'))
        return super().form_valid(form)
from django.http import JsonResponse

def events_json(request):
    events = Event.objects.all()
    data = []
    for event in events:
        data.append({
            "title": event.name,
            "start": event.start_date.isoformat(),
            "end": event.end_date.isoformat(),
            "color": event.color,
            "description": event.description,  
            "url": event.get_absolute_url()
        })
    return JsonResponse(data, safe=False)


def monthly_events(request, year=None, month=None):
    """
    View for displaying events in a specific month.
    """
    if year is None or month is None:
        now = timezone.now()
        year = now.year
        month = now.month
    
    # Get the first and last day of the month
    first_day = datetime(year, month, 1)
    _, last_day_of_month = monthrange(year, month)
    last_day = datetime(year, month, last_day_of_month, 23, 59, 59)
    
    # Convert to aware datetime objects
    first_day = timezone.make_aware(first_day)
    last_day = timezone.make_aware(last_day)
    
    # Get events in this month
    events = Event.objects.filter(
        start_date__gte=first_day,
        start_date__lte=last_day
    ).order_by('start_date')
    
    # Get month name and calendar data
    month_name = calendar.month_name[month]
    cal = calendar.monthcalendar(year, month)
    
    # Get previous and next month for navigation
    prev_month = month - 1
    prev_year = year
    if prev_month == 0:
        prev_month = 12
        prev_year -= 1
    
    next_month = month + 1
    next_year = year
    if next_month == 13:
        next_month = 1
        next_year += 1
    
    # Get today's date for highlighting the current day in the calendar
    today = timezone.now()
    today_date = today.strftime('%Y-%m-%d')
        
    return render(request, 'events/monthly_events.html', {
        'events': events,
        'month_name': month_name,
        'year': year,
        'calendar': cal,
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
        'current_month': month,
        'today_date': today_date,
    })
