from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from mixins.ViewTitleMixin import ViewTitleMixin
# Create your views here.

from django import forms

from email_sender import EmailSender

import os

class NameForm(forms.Form):
    your_name = forms.CharField(label="Nafn", max_length=100)
    email = forms.EmailField(label="Netfang")




class Umsokn(ViewTitleMixin, View):
    name = "dashboard"
    title = "Myntsafnarafélag Íslands"
    
    template_name = 'frontpage/umsokn.html'
    def get(self, request):
        return self.render(request, self.template_name, {"form":NameForm})

    def post(self, request):
        form = NameForm(request.POST)
        print("got request for joining")
        if form.is_valid():
            print(form)
            print(form.cleaned_data)
            print(os.getenv("SERVICE_EMAIL"), os.getenv("SERVICE_EMAIL_PASSWD"))
            EmailSender().send_email("Request for joining", form.cleaned_data, [os.getenv("SIGNUP_RECEIVER")])
        else:
            print("invalid form")
        return self.render(request, self.template_name, {})
