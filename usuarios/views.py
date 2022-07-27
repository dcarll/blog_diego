from django.shortcuts import render

# Create your views here.
from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm

def cadastro(request):
    if request.method == 'POST':
        form = CustomUsuarioCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cadastro.html', {'form': form})
    else:
        form = CustomUsuarioCreateForm()
    return render(request, 'cadastro.html', {'form': form})