from django.views.generic import TemplateView, ListView
from .models import Post 
 
class HomePageView(ListView):
    template_name = 'home.html'
    model = Post

class AboutPageView(TemplateView): # новое
    template_name = 'about.html'