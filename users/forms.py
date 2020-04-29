from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):

        fields = UserCreationForm.Meta.fields + ('age',)
        model = CustomUser


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):

        fields = UserChangeForm.Meta.fields
        model = CustomUser