from django.shortcuts import render
from . models import Contact
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.edit import CreateView

# Create your views here.



class HomePageView(ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'


class ContactCreateView(CreateView):

    model = Contact
    template_name = 'new.html'
    fields = ['name','email','phone','image','stream','video']
   
    success_url = 'success'


class ContactSuccessView(ListView):
     template_name= 'success.html'
     model = Contact
     context_object_name = 'contacts'

class ContactRetrievalView(ListView):
     template_name= 'detail.html'
     model = Contact
     context_object_name = 'contacts' 
