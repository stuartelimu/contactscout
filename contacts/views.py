from django.views.generic import ListView
from .models import Contact

class ContactList(ListView):
    model = Contact