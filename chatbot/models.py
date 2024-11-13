from django.db import models
from django.contrib.auth import get_user_model

class Thread(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='chat_threads'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Chat with {self.user.username} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"

    class Meta:
        ordering = ['-updated_at']

class Message(models.Model):
    SENDER_CHOICES = [
        ('USER', 'User'),
        ('AI', 'AI Assistant')
    ]

    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    content = models.TextField()
    sender_type = models.CharField(
        max_length=4,
        choices=SENDER_CHOICES
    )
    ai_model = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0
    )
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender_type}: {self.content[:50]}..."

    class Meta:
        ordering = ['created_at']
