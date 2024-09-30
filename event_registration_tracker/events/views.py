from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Event, Registration, Feedback
from .forms import FeedbackForm
from django import forms

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        }

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    participant = getattr(request.user, 'participant', None)

    if request.method == 'POST':
        if not participant:
            return render(request, 'events/register_event.html', {'event': event, 'error': 'You do not have a participant profile.'})

        if Registration.objects.filter(participant=participant, event=event).exists():
            return render(request, 'events/register_event.html', {'event': event, 'error': 'You are already registered for this event.'})

        Registration.objects.create(participant=participant, event=event)
        return redirect('registration_success')

    return render(request, 'events/register_event.html', {'event': event})

def event_feedback(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    participant = getattr(request.user, 'participant', None)

    if event.status != 'completed':
        return render(request, 'events/event_feedback.html', {'event': event, 'error': 'Feedback can only be given for completed events.'})

    if request.method == 'POST':
        if not participant:
            return render(request, 'events/event_feedback.html', {'event': event, 'error': 'You do not have a participant profile.'})

        if Feedback.objects.filter(participant=participant, event=event).exists():
            return render(request, 'events/event_feedback.html', {'event': event, 'error': 'You have already provided feedback for this event.'})

        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.participant = participant
            feedback.event = event
            feedback.save()
            return redirect('feedback_success')

    else:
        form = FeedbackForm()

    return render(request, 'events/event_feedback.html', {'event': event, 'form': form}) 

def feedback_success():
    return render(request, 'events/feedback_success.html')

def registration_success():
    return render(request, 'events/registration_success.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid() and form.cleaned_data['password1'] == form.cleaned_data['password2']:
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            auth_login(request, user)
            return redirect('login/')
    else:
        form = RegistrationForm()

    return render(request, 'events/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('event_list/')
    else:
        form = AuthenticationForm()

    return render(request, 'events/login.html', {'form': form})