from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                settings.DEFAULT_FROM_EMAIL,
                [
                    request.POST.get('email')
                ]
            )
            pass
        pass
    else:
        form = ContactForm()
        return render(request, 'contact/contact_form.html', {
            'forms': form,
        })



def thanks(request):
    return HttpResponse('thanks')
