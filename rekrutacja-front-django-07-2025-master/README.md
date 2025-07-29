# System Zarządzania Wydarzeniami

System do zarządzania wydarzeniami, umożliwiający tworzenie i przeglądanie wydarzeń.

## Spis treści

1. [Ogólne informacje](#ogólne-informacje)
2. [Technologie](#technologie)
3. [Instalacja](#instalacja)
4. [Struktura projektu](#struktura-projektu)
5. [Modele danych](#modele-danych)
6. [Widoki](#widoki)
7. [Testy](#testy)
8. [Zadanie rekrutacyjne dla frontend developera](#zadanie-rekrutacyjne-dla-frontend-developera)

## Ogólne informacje

System Zarządzania Wydarzeniami to aplikacja webowa oparta na Django, która umożliwia:
- Przeglądanie nadchodzących wydarzeń
- Wyświetlanie szczegółowych informacji o wydarzeniach
- Tworzenie nowych wydarzeń
- Przeglądanie wydarzeń w formie kalendarza miesięcznego

## Technologie

* Python 3.10+
* Django 4.2+
* HTML/CSS/JavaScript
* Bootstrap 5
* SQLite (baza danych)

## Instalacja

### Wymagania wstępne

* Python 3.10 lub nowszy
* pip (menedżer pakietów Pythona)
* virtualenv (opcjonalnie, ale zalecane)

### Kroki instalacji

1. Sklonuj repozytorium:
   ```
   git clone https://github.com/Dzial-Promocji-UwS/rekrutacja-front-django-04-2025.git
   cd rekrutacja-front-django-04-2025
   ```

2. Utwórz i aktywuj wirtualne środowisko:
   
   Windows:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
   
   Linux/macOS:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. Zainstaluj zależności:
   ```
   pip install -r requirements.txt
   ```

4. Wykonaj migracje bazy danych:
   ```
   python manage.py migrate
   ```

5. Utwórz superużytkownika (opcjonalnie):
   ```
   python manage.py createsuperuser
   ```
   
   Alternatywnie możesz użyć przygotowanego konta administratora:
   - Login: `admin`
   - Hasło: `admin`

6. Uruchom serwer deweloperski:
   ```
   python manage.py runserver
   ```

7. Otwórz przeglądarkę i przejdź do adresu `http://127.0.0.1:8000/`

## Struktura projektu

```
event_manager/           # Główny katalog projektu Django
├── event_manager/       # Konfiguracja projektu
│   ├── __init__.py
│   ├── settings.py      # Ustawienia projektu
│   ├── urls.py          # Główne URLe projektu
│   ├── asgi.py
│   └── wsgi.py
├── events/              # Aplikacja do zarządzania wydarzeniami
│   ├── __init__.py
│   ├── admin.py         # Konfiguracja panelu administracyjnego
│   ├── apps.py
│   ├── forms.py         # Formularze
│   ├── migrations/      # Migracje bazy danych
│   ├── models.py        # Modele danych
│   ├── tests.py         # Testy
│   ├── urls.py          # URLe aplikacji
│   └── views.py         # Widoki aplikacji
├── templates/           # Szablony HTML
│   ├── base.html        # Bazowy szablon
│   └── events/          # Szablony specyficzne dla wydarzeń
│       ├── index.html
│       ├── event_detail.html
│       ├── event_form.html
│       └── monthly_events.html
├── static/              # Pliki statyczne
│   ├── ownassets/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── script.js
├── manage.py            # Skrypt zarządzania Django
└── requirements.txt     # Zależności projektu
```

## Modele danych

### Event (Wydarzenie)

Model reprezentujący wydarzenie w systemie.

Atrybuty:
- `name` - nazwa wydarzenia
- `description` - opis wydarzenia
- `start_date` - data i czas rozpoczęcia
- `end_date` - data i czas zakończenia
- `location` - lokalizacja
- `mode` - tryb wydarzenia (stacjonarny/zdalny)
- `organizer` - organizator
- `color` - kolor przypisany do wydarzenia
- `capacity` - maksymalna liczba uczestników
- `created_at` - data utworzenia

## Widoki

### Podstawowe widoki:

1. **Index** (`/`) - strona główna z listą nadchodzących wydarzeń
2. **Event Detail** (`/events/<id>/`) - szczegóły wydarzenia
3. **Event Create** (`/events/create/`) - formularz tworzenia nowego wydarzenia
4. **Event Edit** (`/events/<id>/edit/`) - formularz edycji istniejącego wydarzenia
5. **Monthly Events** (`/events/monthly/` lub `/events/monthly/<year>/<month>/`) - widok kalendarza miesięcznego

## Testy

Projekt zawiera testy jednostkowe dla modeli i widoków. Można je uruchomić za pomocą:

```
python manage.py test events
```

### Rodzaje testów:

1. **EventModelTests** - testy modelu Event
2. **EventViewTests** - testy widoków związanych z wydarzeniami

### Uruchamianie konkretnych testów:

```
# Uruchomienie konkretnej klasy testów
python manage.py test events.tests.EventModelTests

# Uruchomienie konkretnego testu
python manage.py test events.tests.EventModelTests.test_event_creation
```

### Testowanie pokrycia kodu:

Można sprawdzić pokrycie kodu testami za pomocą pakietu `coverage`:

```
# Instalacja coverage
pip install coverage

# Uruchomienie testów z pomiarem pokrycia
coverage run --source='.' manage.py test events

# Wygenerowanie raportu
coverage report

# Opcjonalnie, wygenerowanie raportu HTML
coverage html
```

## Opis zadania rekrutacyjnego

W katalogu `templates/events/` znajdują się szablony zadań rekrutacyjnych. Każdy szablon zawiera szczegółowy opis zadania, dane przekazywane do szablonu oraz wymagania implementacyjne.

### Uruchomienie 

1. Sklonuj repozytorium i zainstaluj zależności zgodnie z instrukcjami w sekcji [Instalacja](#instalacja)
2. Uruchom serwer deweloperski:
   ```
   python manage.py runserver
   ```
3. Otwórz przeglądarkę i przejdź do adresu `http://127.0.0.1:8000/`
4. Przeglądaj dostępne widoki, aby zapoznać się z funkcjonalnością aplikacji:
   - Strona główna: `http://127.0.0.1:8000/`
   - Szczegóły wydarzenia: `http://127.0.0.1:8000/events/1/`
   - Formularz tworzenia wydarzenia: `http://127.0.0.1:8000/events/create/`
   - Kalendarz miesięczny: `http://127.0.0.1:8000/events/monthly/`

### Zadania do implementacji

W ramach zadania rekrutacyjnego należy zaimplementować następujące cztery szablony frontendowe, zgodnie z wytycznymi zawartymi w plikach:

1. `index.html` - Strona główna systemu
2. `event_detail.html` - Szczegóły wydarzenia
3. `event_form.html` - Formularz tworzenia/edycji wydarzenia
4. `monthly_events.html` - Kalendarz miesięczny wydarzeń

Każdy szablon zawiera dokładny opis zadania, wymagania i dane przekazywane z backendu. Do implementacji kalendarza w `monthly_events.html` można wykorzystać dowolny framework JavaScript (np. FullCalendar, Calendar.js).

### ZADANIA:

1. **Strona główna** (`index.html`) - implementacja strony głównej systemu z sekcją powitalną i listą nadchodzących wydarzeń.
   - Wyświetlanie podstawowych informacji o systemie
   - Prezentacja nadchodzących wydarzeń w postaci kart
   - Przyciski nawigacyjne do innych widoków

2. **Szczegóły wydarzenia** (`event_detail.html`) - implementacja strony z szczegółowymi informacjami o wydarzeniu.
   - Pełne informacje o wydarzeniu (nazwa, opis, data, lokalizacja, organizator)

3. **Formularz wydarzenia** (`event_form.html`) - implementacja formularza do tworzenia i edycji wydarzeń.
   - Podział na logiczne sekcje za pomocą fieldsetów
   - Pola formularza z odpowiednimi etykietami i oznaczeniami wymagalności
   - Obsługa walidacji pól i wyświetlanie błędów

4. **Kalendarz miesięczny** (`monthly_events.html`) - implementacja kalendarza z widokiem miesięcznym wydarzeń.
   - Siatka kalendarza z dniami miesiąca
   - Wydarzenia wyświetlane w odpowiednich dniach
   - Nawigacja między miesiącami
   - Lista wydarzeń w bieżącym miesiącu
   - Możliwość użycia dowolnego frameworka JavaScript do kalendarzy (np. FullCalendar, Calendar.js)

### Wymagania dotyczące zadań frontendowych:

- Wszystkie komponenty UI muszą być oparte na Bootstrap 5
- Implementacja musi być w pełni zgodna ze standardami WCAG AAA
- Design musi być responsywny i dostosowany do różnych urządzeń
- Stylizacja zgodna z księgą znaku Uniwersytetu w Siedlcach (kolor marki #003d7c)
- Wszystkie teksty muszą być zawinięte w tagi tłumaczeń Django
- Formularze muszą zawierać właściwe oznaczenia pól wymaganych i komunikaty błędów
- Elementy interaktywne muszą być dostępne z klawiatury
- Kontrast kolorystyczny musi spełniać wymagania WCAG AAA (7:1)

Każde zadanie zawiera szczegółowe informacje o danych przekazywanych do szablonu, elementach do zaimplementowania oraz wytycznych dotyczących dostępności.



## \*Zadanie dodatkowe: Wdrożenie narzędzi wspierających dostępność (funkcje typu [UserWay](https://userway.org/))



### Cel

Wdrożenie zestawu funkcjonalności wspierających dostępność strony internetowej, umożliwiających użytkownikom dostosowanie sposobu wyświetlania treści. Rozwiązania mają na celu poprawę użyteczności serwisu dla osób z niepełnosprawnością wzroku lub trudnościami w czytaniu.

Przykładowy zakres prac udostępniono poniżej, natomiast implementacja końcowa zależy jedynie od Ciebie. Jeżeli uważasz, że jakieś funkcje są zbędne lub dodatkowo potrzebne, pozostawiamy Ci dowolność.



Uwaga! 

Narzędzie musi być w pełni zgodne ze standardami WCAG AAA.

---

### Przykładowy zakres prac

#### 1. Widoczny widget dostępności

- Umieszczenie w stałym miejscu (np. prawy górny róg) ikony lub przycisku otwierającego panel dostępności.
- Pełna obsługa przy pomocy klawiatury i czytników ekranu (ARIA, role, focus management).

#### 2. Zmiana rozmiaru tekstu

#### 3. Zmiana kontrastu kolorystycznego

#### 4. Wyłączenie animacji

#### 5. Zapamiętywanie preferencji użytkownika

#### 6. Skróty klawiszowe do obsługi widgetu

#### 7. Testy i zgodność z WCAG (warunek konieczny - całość musi być zgodna z WCAG na poziomie AAA)



