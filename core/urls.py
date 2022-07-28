from django.urls import path
from .views import IndexView, LoginView, CadastroView, PostView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('post/', PostView.as_view(), name='post'),
    path('about/', AboutView.as_view(), name='about'),
]