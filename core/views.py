from django.shortcuts import render
from django.views import generic

# Create your views here.
class HomeView(generic.TemplateView):
    """
    website home page
    **Template**
    :template:`core/index.html`
    """
    template_name = 'core/index.html'


