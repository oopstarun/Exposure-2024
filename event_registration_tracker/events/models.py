# models.py

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def is_full(self):
        return self.registration_set.count() >= self.capacity if self.capacity else False

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='participant_pictures/', null=True, blank=True)

class Registration(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('participant', 'event')

class Feedback(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('participant', 'event')
