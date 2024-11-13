from django.shortcuts import render
from rest_framework import mixins, viewsets
from .models import Thread, Message
from .serializers import ThreadSerializer, MessageSerializer

# Create your views here.

class ThreadViewSet(viewsets.ModelViewSet):
    serializer_class = ThreadSerializer

    def get_queryset(self):
        return Thread.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MessageViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(thread__user=self.request.user)

    def perform_create(self, serializer):
        thread = Thread.objects.get(pk=self.kwargs['thread_pk'])
        serializer.save(thread=thread)
