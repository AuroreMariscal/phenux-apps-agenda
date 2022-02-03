from django.shortcuts import render
from .models import Event
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        return Event.objects.all()


class DetailView(generic.DetailView):
    model = Event
    template_name = 'event.html'
