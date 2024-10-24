from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Event, Category
from .forms import EventForm


def all_events(request):
    """
    A view to show all events,
    including sorting,
    search queries, and filters
    """

    # Get all events
    events = Event.objects.all().order_by('pk')

    # Initialize query, sorting, and direction
    query = None
    sort = None
    direction = None
    category = None
    special = None

    # Handle sorting
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

    # Handle search queries
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('all_events'))

        queries = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query) |
            Q(category__name__icontains=query)
        )
        events = events.filter(queries)

    # Handle category filtering
    if 'category' in request.GET:
        category = request.GET['category']
        if category != 'all':
            try:
                # Get the Category object
                category_instance = Category.objects.get(id=category)
                # Filter by the Category instance
                events = events.filter(category=category_instance)
            except Category.DoesNotExist:
                messages.error(request, "Selected category does not exist.")
                return redirect(reverse('all_events'))

    # Fetch all categories for navbar
    categories = Category.objects.all()

    # Construct current sorting string for context
    current_sorting = (
        f'{sort}_{direction}'
        if sort and direction
        else 'None_None'
    )

    context = {
        'events': events,
        'search_term': query,
        'current_sorting': current_sorting,
        'current_category': category,
        'current_special': special,
        'current_categories': categories,  # Add this line
    }

    return render(request, 'events/events.html', context)


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    context = {
        'event': event,
    }
    return render(request, 'events/event_detail.html', context)


def add_event(request):

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Successfully added Event!')
            return redirect(reverse('event_detail', args=[event.id]))
        else:
            messages.error(
                request,
                'Failed to add Event. Please ensure the form is valid.'
            )
    else:
        form = EventForm()

    template = 'events/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_event(request, event_id):
    """ Edit an event in the store """
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            # Redirect to the event detail page
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)

    return render(request, 'events/edit_event.html',
                  {'form': form, 'event': event})


def delete_event(request, event_id):
    """ Delete an event from the store """
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, 'Event deleted!')
    return redirect(reverse('all_events'))
