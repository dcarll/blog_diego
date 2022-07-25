
from django.views.generic import TemplateView

#criação das views

#view index
class IndexView(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
	template_name = 'login.html'
