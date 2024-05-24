from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from mixins.ViewTitleMixin import ViewTitleMixin
# Create your views here.

class Uppbod(ViewTitleMixin, View):
    name = "dashboard"
    title = "Myntsafnarafélag Íslands"
    
    template_name = 'frontpage/uppbod.html'
    def get(self, request):
        return self.render(request, self.template_name, {})