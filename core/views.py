
from django.views.generic import TemplateView, FormView, ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q
from .forms import PostForm

from .models import Sobre, Post

#criação das views

def post_list(request):
	template_name = 'post.html'
	objects = Post.objects.all()
	search = request.GET.get('search')
	if search:
		objects = objects.filter(post__icontains=search)
	context = {'object_list': objects}
	return render(request, template_name, context)

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
	paginate_by = 2

	def query_set(self):
		queryset = super(PostView, self).get_queryset()
		search = self.request.GET.get('search')
		if search:
			queryset = queryset.filter(
				Q(post__icontains)
				)

class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'
    paginate_by = 2

    def get_queryset(self):
        queryset = super(PostList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(post__icontains=search) 
                
            )
        return queryset
	

class AboutView(ListView):
	template_name = 'about.html'
	model = Sobre
	queryset = Sobre.objects.all()
	context_object_name = 'sobre'

class PostDetalhesView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'produto'

    
