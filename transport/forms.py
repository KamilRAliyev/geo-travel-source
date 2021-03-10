from django import forms


class CarRentalForm(forms.Form):
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

    start_date = forms.CharField(widget=forms.TextInput(attrs={
        'class': "input form-control",
        'placeholder': "mm/dd/yyyy",
        'id': "datepick1",
        # 'onchange': """function asda(){
        #                         let date1_str = $("#datepick1").val();
        #                         let parts = date1_str.split('/');
        #                         mydate = new Date(parts[2], parts[1] - 1, parts[0]);
        #                         if(mydate2){
        #                             price(mydate, mydate2);
        #                         }"""
        # 'onFocus' : "$('#datepick1').datepicker('show');",
    }))

    end_date = forms.CharField(widget=forms.TextInput(attrs={
        'class': "input form-control",
        'placeholder': "mm/dd/yyyy",
        'id': "datepick2",
        # 'onchange': """function sada(){
        #                         let date2_str = $("#datepick2").val();
        #                         let parts2 = date2_str.split('/');
        #                         mydate2 = new Date(parts2[2], parts2[1] - 1, parts2[0]);
        #                         if(mydate){
        #                             price(mydate, mydate2);
        #                         }
        #                     }"""
        # 'onFocus' : "$('#datepick1').datepicker('show');",
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
