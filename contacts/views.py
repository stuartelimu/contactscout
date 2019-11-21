from django.views.generic import ListView, DetailView
from .models import Contact

class ContactList(ListView):
    model = Contact


class ContactDetail(DetailView):
    model = Contact