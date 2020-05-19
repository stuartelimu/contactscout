from django.urls import path
from .views import ContactList, ContactDetail, ContactCreate, ContactUpdate, ContactDelete

urlpatterns = [
    path('contacts/', ContactList.as_view(), name='contact-list'),
    path('contacts/<int:pk>', ContactDetail.as_view(), name='contact-detail'),
    path('contacts/add/', ContactCreate.as_view(), name='contact-add'),
    path('contacts/<int:pk>/update/', ContactUpdate.as_view(), name='contact-edit'),
    path('contacts/<int:pk>/delete/', ContactDelete.as_view(), name='contact-delete'),
]