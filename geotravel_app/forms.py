from django import forms
from .models import ContactFormInfo

class ContactForm(forms.Form):
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

    subject = forms.CharField(widget=forms.TextInput(attrs={
        'value': 'Subject',
        'class': "form-control",
        'onblur': "if(this.value=='') this.value='Subject'",
        'onFocus': "if(this.value =='Subject' ) this.value=''"
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'value': 'Message',
        'class': "form-control",
        'rows': '11',
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
        model = ContactFormInfo
        fields = ('name', 'email', 'subject', 'message')


class EvisaForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={
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

    number = forms.CharField(widget=forms.TextInput(attrs={
        'value': 'Phone Number',
        'class': "form-control",
        'onblur': "if(this.value=='') this.value='Phone Number'",
        'onFocus': "if(this.value =='Phone Number' ) this.value=''"
    }))

    passport = forms.FileField(widget=forms.FileInput(attrs={
        "type":"file",
        'class':"custom-file-input",
        'accept': '.jpg, .jpeg, .png, .pdf'
    }))
    document = forms.FileField(widget=forms.FileInput(attrs={
        "type": "file",
        'class': "custom-file-input",
        'accept': '.jpg, .jpeg, .png, .pdf'
    }))
