from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import widgets

User = get_user_model()




class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label= ("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class CreateTask(forms.ModelForm):
    text = forms.CharField(max_length=50, label='Write your task')
    complete = forms.BooleanField(label='Complete')
    class Meta:
        model = User
        fields = ('text',)



class DeleteTask(forms.ModelForm):
    id = forms.IntegerField(label='ID:')
    class Meta:
        model = User
        fields = ('id', )
