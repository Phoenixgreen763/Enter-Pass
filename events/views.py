from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Event

def all_events(request):
    """ A view to show all events, including sorting and search queries """
    
    events = Event.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                events = events.annotate(lower_title=Lower('title'))
            if sortkey == 'date':
                sortkey = 'date'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            events = events.order_by(sortkey)
            
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('events'))
            
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            events = events.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'events': events,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'events/events.html', context)

def events_by_price(request):
    events = Event.objects.all().order_by('price')  # Assuming you add a price field to Event model
    return render(request, 'events.html', {'events': events})

def events_by_rating(request):
    events = Event.objects.all().order_by('-rating')  # Assuming you add a rating field to Event model
    return render(request, 'events.html', {'events': events})

def events_by_category(request, category):
    events = Event.objects.filter(category=category)
    return render(request, 'events.html', {'events': events})

def events_special(request, special):
    if special == 'new':
        events = Event.objects.filter(date__gte=date.today())  # Example filter for new events
    elif special == 'deals':
        events = Event.objects.filter(discount__gt=0)  # Example filter for deals
    elif special == 'group':
        events = Event.objects.filter(group_offer=True)  # Example filter for group offers
    else:
        events = Event.objects.all()
    return render(request, 'events.html', {'events': events})
