from django.urls import path
from .views import IndexView, LoginView, CadastroView, PostView, AboutView, PostList, PostDetalhesView

app_name = 'post'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('post/<int:pk>/', PostDetalhesView.as_view(), name='post_detail'),
    path('posts/', PostList.as_view(), name='posts'),
    path('about/', AboutView.as_view(), name='about'),
    
]