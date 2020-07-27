from django import forms
from django.contrib.auth.models import User
from .models import ContactUsInfo,Result
from django.contrib.auth.password_validation import validate_password


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(),validators=[validate_password])
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm_password does not match"
            )

class ContactUsForm(forms.ModelForm):
    message = forms.CharField( widget=forms.Textarea(attrs={'overflow-y': 'scroll','style':'resize:none;'}) )
    class Meta:
        model = ContactUsInfo
        fields = "__all__"

class ResultForm(forms.ModelForm):
    class Meta:
        model=Result
        fields="__all__"
