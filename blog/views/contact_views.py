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
        # Set the "thank you" message in the context

        self.request.session['form_submitted'] = True

        return super().form_valid(form)

    def form_invalid(self, form):
        # If the form is invalid, you can handle it here
        # You can either display an error message or redirect the user back to the form

        # For example, you can render the form again with error messages
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add a "thank you" message to the context

        if self.request.session.pop('form_submitted', False):
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