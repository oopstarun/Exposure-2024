from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Registration, Participant, Feedback

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = []

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comments']
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 4}),
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    preferences = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Preferences', 'rows': 4})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Ensure these are the correct fields

    def save(self, commit=True):
        user = super().save(commit=commit)  # Call the parent's save method to create the user
        profile = Profile(user=user, preferences=self.cleaned_data.get('preferences'))
        if commit:
            profile.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True, 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
