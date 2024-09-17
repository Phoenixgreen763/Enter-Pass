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
