from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Snack

# Create your views here.
class Snack_List_View(ListView):
    template_name='snack_list.html'
    model = Snack
    context_object_name = 'snacks'

class Snack_Detail_View(DetailView):
    template_name='snack_detail.html'
    model = Snack
    