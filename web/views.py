from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cars, ContactForm
from .forms import ContactFormForm
from django.contrib.auth.decorators import login_required

def indice(request):
    public_cars = Cars.objects.filter(is_private=False)

    return render(
        request,
        'index.html',
        {
            'public_cars': public_cars
        }
)

def acerca(request):
    return render(request, 'about.html', {})

@login_required
def bienvenido(request):
    private_cars = Cars.objects.filter(is_private=True)

    return render(
        request,
        'welcome.html',
        {
            'private_cars': private_cars
        }
    )

def contacto(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactFormForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            contact_form = ContactForm.objects.create(**form.cleaned_data)

            # redirect to a new URL:
            return HttpResponseRedirect('/exito')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactFormForm()

    return render(request, 'contactus.html', {'form': form})


def exito(request):
    return render(request, 'success.html', {})
