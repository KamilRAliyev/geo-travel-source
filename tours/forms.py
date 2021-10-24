from django import forms
from .models import TourPriceTable




class TourCommentForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'value': 'Full Name',
        'onblur': "if(this.value=='') this.value='Full Name'",
        'onfocus': "if(this.value =='Full Name' ) this.value=''"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'value': 'Email address',
        'class': "form-control",
        'onblur': "if(this.value=='') this.value='Email address'",
        'onFocus': "if(this.value =='Email address' ) this.value=''"
    }))

    comment = forms.CharField(widget=forms.Textarea( attrs={
        "class": "form-control",
        'rows': "9",
        'id': "inputMessage",
        'name': "content",
        'onblur': "if(this.value=='') this.value='Your Comment'",
        'onfocus': "if(this.value =='Your Comment' ) this.value=''",
        'placeholder': 'Your Comment'
    }))


