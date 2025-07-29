from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/create/', views.EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('events/<int:pk>/edit/', views.EventUpdateView.as_view(), name='event_update'),
    path('events/monthly/', views.monthly_events, name='monthly_events'),
    path('events/monthly/<int:year>/<int:month>/', views.monthly_events, name='monthly_events_date'),
    path('events/json/', views.events_json, name='events_json'),

] 