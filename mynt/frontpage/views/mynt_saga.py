from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from mixins.ViewTitleMixin import ViewTitleMixin
# Create your views here.

class MyntSaga(ViewTitleMixin, View):
    name = "myntSaga"
    title = "Myntsafnarafélag Íslands"
    
    template_name = 'frontpage/sedlasaga.html'
    def get(self, request):
        
        return self.render(request, self.template_name, {})