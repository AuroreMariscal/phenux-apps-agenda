from django.shortcuts import render, get_object_or_404
from .models import Event
from django.views import generic


class ListView(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Event.objects.all()


class DetailView(generic.DetailView):
    model = Event
    template_name = 'event.html'

    def results(request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        return render(request, 'events.html', {'event': event})
