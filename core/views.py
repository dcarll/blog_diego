
from django.views.generic import TemplateView

#criação das views

#view index
class IndexView(TemplateView):
    template_name = 'index.html'
