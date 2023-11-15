from django.urls import reverse
from django.shortcuts import render
from django.views.generic import FormView

from ..forms import ContactForm

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'blog/contact.html'
    # success_url = '/'
    def get_success_url(self):
        return reverse('contact')
    
