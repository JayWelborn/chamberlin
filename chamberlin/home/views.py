# Django imports
from django.views.generic import TemplateView, ListView, FormView
from django.contrib.messages.views import SuccessMessageMixin

# Relative imports
from .models import Home, About, Contact
from .forms import ContactForm


# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        """
        Return data from most recent update to home info in database.
        """
        context = super(IndexView, self).get_context_data(**kwargs)
        context['home'] = Home.objects.latest('pub_date')
        return context


class AboutView(ListView):
    template_name = 'home/about.html'
    context_object_name = 'about'
    model = About

    def get_queryset(self):
        return About.objects.latest('pub_date')


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'home/contact.html'
    form_class = ContactForm
    success_url = '/contact/'
    success_message = 'Thanks for the Email!'

    def get_context_data(self, **kwargs):
        """
        Get list of info from Contact Model to be passed to view
        :return: latest contact information from db
        """
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contact_info'] = Contact.objects.latest('pub_date')
        return context

    def form_valid(self, form):
        """
        Sends email and displays success message when a valid form
        is submitted.
        :param form: from .forms.py
        :return: instance of ContactView with success_msg attribute accessible for the view.
        """
        form.send_email()
        return super(ContactView, self).form_valid(form)
