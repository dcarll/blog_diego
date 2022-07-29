
from django.views.generic import TemplateView, FormView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView



from .models import Sobre, Post

#criação das views

#view index
class IndexView(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
	template_name = 'login.html'

class CadastroView(TemplateView):
	template_name = 'cadastro.html'

class PostView(ListView):
	template_name = 'post.html'
	model = Post
	queryset = Post.objects.all()
	context_object_name = 'post'


	

class AboutView(ListView):
	template_name = 'about.html'
	model = Sobre
	queryset = Sobre.objects.all()
	context_object_name = 'sobre'

