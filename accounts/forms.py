from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=20,required=False)
    last_name=forms.CharField(max_length=20,required=False)
    email=forms.EmailField(required=True,help_text="please enter a valid email")

    class Meta:
        model=User
        fields=('username','first_name','last_name','password1','password2','email')