# from django.forms import ModelForm
from django.core.validators import validate_slug, validate_email
from django import forms
from .validators import validate_domainonly_email
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'content']

        widgets = {
            'name': forms.TextInput(),
            'email': forms.EmailInput(),
            'content': forms.Textarea()
        }



# class ContactForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField(validators=[validate_domainonly_email])
#     content = forms.CharField(widget=forms.Textarea())

#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass

#     # def clean_<field_name>(self):
#     #     "validate here"
#     #     return "field_name_passed_value"

#     # def clean_email(self):
#     #     # field validation - field error
#     #     email_passed = self.cleaned_data.get("email")
#     #     # email_req = "mydomain.com"

#     #     # if not email_req in email_passed:
#     #     #     raise forms.ValidationError("Not a valid email. Please try again")
#     #     return email_passed
    
#     # def clean(self):
#     #     # form validation
#     #     cleaned_data = super(ContactForm, self).clean()
#     #     email_passed = cleaned_data.get("email")

#     #     # email_req = "mydomain.com"

#     #     # if not email_req in email_passed:
#     #     #     raise forms.ValidationError("Not a valid email. Please try again")