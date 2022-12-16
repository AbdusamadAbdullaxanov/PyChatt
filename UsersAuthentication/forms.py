from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        fields = ["username", "email", "first_name", "last_name", "password"]
        model = User
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "autofocus": "autofocus",
                    "class": "u-border-10 u-border-grey-10 u-grey-10 u-input u-input-rectangle u-radius-50 u-input-1",
                    "placeholder": "Enter your Username, no spaces please"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter your email address",
                    "class": "u-border-10 u-border-grey-10 u-grey-10 u-input u-input-rectangle u-radius-50 u-input-4"
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter Your First Name",
                    "class": "u-border-10 u-border-grey-10 u-grey-10 u-input u-input-rectangle u-radius-50 u-input-2"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter Your Last Name",
                    "class": "u-border-10 u-border-grey-10 u-grey-10 u-input u-input-rectangle u-radius-50 u-input-3"
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "placeholder": "Suggest strong password",
                    "class": "u-border-10 u-border-grey-10 u-grey-10 u-input u-input-rectangle u-radius-50 u-input-5"
                }
            )
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your Username",
                "class": "u-border-10 u-border-grey-10 u-grey-10 u-input u-input-rectangle u-radius-50 u-input-1",

            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter your email address",
                "class": "u-border-10 u-border-grey-10 u-grey-10 u-input u-input-rectangle u-radius-50 u-input-2",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your Password",
                "class": "u-border-10 u-border-grey-10 u-grey-10 u-input u-input-rectangle u-radius-50 u-input-3"
            }
        )
    )
