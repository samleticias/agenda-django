from django.contrib import messages
from contact.forms import RegisterForm
from django.shortcuts import redirect, render


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )