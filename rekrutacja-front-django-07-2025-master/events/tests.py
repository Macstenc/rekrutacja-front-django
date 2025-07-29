from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .models import Event

class EventModelTests(TestCase):
    """
    Testy dla modelu Event sprawdzające poprawność jego funkcjonalności.
    """
    
    def setUp(self):
        """Konfiguracja początkowa do wszystkich testów."""
        self.event_data = {
            'name': 'Test Event',
            'description': 'This is a test event',
            'start_date': timezone.now() + timedelta(days=1),
            'end_date': timezone.now() + timedelta(days=1, hours=2),
            'location': 'Test Location',
            'mode': 'in_person',
            'organizer': 'Test Organizer',
            'color': '#003d7c',
            'capacity': 10
        }
        self.event = Event.objects.create(**self.event_data)
    
    def test_event_creation(self):
        """Test czy wydarzenie zostało poprawnie utworzone."""
        self.assertEqual(self.event.name, 'Test Event')
        self.assertEqual(self.event.organizer, 'Test Organizer')
        self.assertEqual(self.event.capacity, 10)
    
    def test_event_str_method(self):
        """Test czy metoda __str__ zwraca oczekiwaną nazwę wydarzenia."""
        self.assertEqual(str(self.event), 'Test Event')
    
    def test_event_get_absolute_url(self):
        """Test czy metoda get_absolute_url zwraca poprawny URL."""
        expected_url = reverse('event_detail', args=[self.event.id])
        self.assertEqual(self.event.get_absolute_url(), expected_url)
    
    def test_is_past_for_future_event(self):
        """Test czy metoda is_past zwraca False dla przyszłego wydarzenia."""
        self.assertFalse(self.event.is_past)
    
    def test_is_past_for_past_event(self):
        """Test czy metoda is_past zwraca True dla przeszłego wydarzenia."""
        past_event = Event.objects.create(
            name='Past Event',
            description='This is a past event',
            start_date=timezone.now() - timedelta(days=2),
            end_date=timezone.now() - timedelta(days=2, hours=2),
            location='Past Location',
            mode='remote',
            organizer='Past Organizer',
            color='#FF0000',
            capacity=5
        )
        self.assertTrue(past_event.is_past)

class EventViewTests(TestCase):
    """
    Testy widoków związanych z modelami Event.
    """
    
    def setUp(self):
        """Konfiguracja początkowa dla testów widoków."""
        self.client = Client()
        
        # Tworzenie przyszłego wydarzenia
        self.future_event = Event.objects.create(
            name='Future Event',
            description='This is a future event',
            start_date=timezone.now() + timedelta(days=1),
            end_date=timezone.now() + timedelta(days=1, hours=2),
            location='Future Location',
            mode='in_person',
            organizer='Future Organizer',
            color='#003d7c',
            capacity=10
        )
        
        # Tworzenie przeszłego wydarzenia
        self.past_event = Event.objects.create(
            name='Past Event',
            description='This is a past event',
            start_date=timezone.now() - timedelta(days=2),
            end_date=timezone.now() - timedelta(days=2, hours=2),
            location='Past Location',
            mode='remote',
            organizer='Past Organizer',
            color='#FF0000',
            capacity=5
        )
    
    def test_index_view(self):
        """Test czy widok index zwraca poprawny status i zawiera przyszłe wydarzenia."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('upcoming_events', response.context)
        self.assertIn(self.future_event, response.context['upcoming_events'])
        self.assertNotIn(self.past_event, response.context['upcoming_events'])
    
    
    def test_event_detail_view(self):
        """Test czy widok szczegółów wydarzenia zwraca poprawny status i dane wydarzenia."""
        response = self.client.get(reverse('event_detail', args=[self.future_event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn('event', response.context)
        self.assertEqual(response.context['event'], self.future_event)
    
    def test_event_create_view_get(self):
        """Test czy widok tworzenia wydarzenia zwraca formularz."""
        response = self.client.get(reverse('event_create'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
    
    def test_event_create_view_post(self):
        """Test czy widok tworzenia wydarzenia poprawnie tworzy nowe wydarzenie."""
        event_data = {
            'name': 'New Test Event',
            'description': 'This is a new test event',
            'start_date': (timezone.now() + timedelta(days=5)).strftime('%Y-%m-%dT%H:%M'),
            'end_date': (timezone.now() + timedelta(days=5, hours=2)).strftime('%Y-%m-%dT%H:%M'),
            'location': 'New Location',
            'mode': 'in_person',
            'organizer': 'New Organizer',
            'color': '#00FF00',
            'capacity': 15
        }
        
        # Wysłanie formularza
        response = self.client.post(reverse('event_create'), event_data, follow=True)
        
        # Sprawdzenie czy formularz został prawidłowo przetworzony
        self.assertEqual(response.status_code, 200)
        
        # Sprawdzenie czy wydarzenie zostało utworzone
        self.assertTrue(Event.objects.filter(name='New Test Event').exists())
    
    def test_event_update_view(self):
        """Test czy widok aktualizacji wydarzenia zawiera poprawne dane."""
        # Zakładamy, że URL to 'event_update' zamiast 'event_edit'
        response = self.client.get(reverse('event_update', args=[self.future_event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertEqual(response.context['form'].instance, self.future_event)
    
    def test_monthly_events_view(self):
        """Test czy widok miesięczny wydarzeń zwraca poprawny status i zawiera kalendarz."""
        # Test bez argumentów (domyślny bieżący miesiąc)
        response = self.client.get(reverse('monthly_events'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('calendar', response.context)
        self.assertIn('month_name', response.context)
        self.assertIn('events', response.context)

# Jak używać testów
"""
Aby uruchomić wszystkie testy, wykonaj polecenie:
    python manage.py test events

Aby uruchomić konkretną klasę testów:
    python manage.py test events.tests.EventModelTests

Aby uruchomić konkretny test:
    python manage.py test events.tests.EventModelTests.test_event_creation

Pokrycie testami można sprawdzić używając pakietu coverage:
1. Zainstaluj coverage: pip install coverage
2. Uruchom testy z coverage: coverage run --source='.' manage.py test events
3. Wygeneruj raport: coverage report
4. Opcjonalnie, wygeneruj raport HTML: coverage html
"""
