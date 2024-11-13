from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

# Create your views here.

@extend_schema_view(
    list=extend_schema(description='Get all events for the authenticated user'),
    create=extend_schema(description='Create a new event'),
    retrieve=extend_schema(description='Get a specific event by ID'),
    update=extend_schema(description='Update an event'),
    destroy=extend_schema(description='Delete an event')
)
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
