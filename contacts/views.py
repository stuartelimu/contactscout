from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contact


class ContactList(ListView):
    model = Contact


class ContactDetail(DetailView):
    model = Contact


class ContactCreate(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['first_name', 'last_name', 'telephone', 'email']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ContactUpdate(UpdateView):
    model = Contact
    fields = ['first_name', 'last_name', 'telephone', 'email']


class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact-list')