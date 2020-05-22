from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError

from . import forms
from . import models

# Create your views here.

class SignUpView(CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

class ChurchDetail(DetailView):
    model = models.CustomUser
    template_name = 'users/church_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['church'] = models.CustomUser.objects.all()
        return context


class ChurchContact(DetailView):
    model = models.CustomUser
    template_name = 'users/church_contact.html'


def emailView(request, pk):

    if request.method == 'GET':
        form = forms.ContactForm()
        church = models.CustomUser.objects.get(pk=pk)
        church_dict = {'church':church}
    else:
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['user']
            from_email = 'noreply@jonezfam.com'
            message = 'From: '+form.cleaned_data['user']+' Email:'+form.cleaned_data['email']+'Phone:'+str(form.cleaned_data['phone'])+' Message:'+form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['timjonez@protonmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, "users/contact.html", {'form': form, 'church':church})
