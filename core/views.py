
from django.views.generic import TemplateView, FormView

#criação das views

#view index
class IndexView(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
	template_name = 'login.html'

class CadastroView(TemplateView):
	template_name = 'cadastro.html'

class PostView(TemplateView):
	template_name = 'post.html'

class AboutView(TemplateView):
	template_name = 'about.html'
