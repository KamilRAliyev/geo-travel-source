from django import forms
from .models import GuideOrder


class GuideForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'value': 'Full Name',
        'class': "form-control",
        'onblur': "if(this.value=='') this.value='Full Name'",
        'onFocus': "if(this.value =='Full Name' ) this.value=''"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'value': 'Email address',
        'class': "form-control",
        'onblur': "if(this.value=='') this.value='Email address'",
        'onFocus': "if(this.value =='Email address' ) this.value=''"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'value': 'Message',
        'class': "form-control",
        'onblur': "if(this.value=='') this.value='Message'",
        'onFocus': "if(this.value =='Message' ) this.value=''"
    }))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "@" in email:
            raise forms.ValidationError("Please write email.")
        if not "." in email:
            raise forms.ValidationError("Please write email.")
        return email

    def clean_name(self):
        fullname = self.cleaned_data.get('name')
        if "@" in fullname:
            raise forms.ValidationError("This field is for fullname. Not for email")
        return fullname

    class Meta:
        model = GuideOrder
        fields = ('name', 'email', 'message')