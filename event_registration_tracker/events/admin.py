# events/admin.py

from django.contrib import admin
from .models import Event, Participant, Registration, Feedback

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'end_time', 'location', 'category')
    search_fields = ('title', 'location', 'category')
    list_filter = ('date', 'category')
    ordering = ('date',)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'preferences')
    search_fields = ('user__email',)

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('participant', 'event', 'registration_date')
    list_filter = ('event',)
    search_fields = ('participant__user__email',)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('participant', 'event', 'rating', 'comments', 'created_at')
    list_filter = ('rating',)
    search_fields = ('participant',)

admin.site.register(Event, EventAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Feedback, FeedbackAdmin)

