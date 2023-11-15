from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic.edit import CreateView

from ..forms import ContactForm
from ..models import Contact

class ContactFormView(FormView):
    model = Contact
    form_class = ContactForm
    template_name = 'blog/contact.html'
    # success_url = '/'
    def get_success_url(self):
        return reverse('contact')
    
    def form_valid(self, form):
        form.save()
        #self.extra_context = {'thank_you_message': 'Thank you for your submission!'} 
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add a "thank you" message to the context
        context['thank_you_message'] = 'Thank you for your submission!'
        return context
# class ContactFormView(CreateView):
#     model = Contact
#     #form_class = ContactForm
#     fields = ['name', 'email', 'content']
#     success_url = reverse_lazy('contact')
#     template_name = 'blog/contact.html'

#     def form_valid(self, form):
#         return super(ContactFormView, self).form_valid(form)