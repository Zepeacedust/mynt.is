from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from mixins.ViewTitleMixin import ViewTitleMixin

from news.models import Post

# Create your views here.

class Index(ViewTitleMixin, View):
    name = "dashboard"
    title = "Myntsafnarafélag Íslands"
    
    template_name = 'news/overview.html'
    def get(self, request):
        posts = Post.objects.all()
        return self.render(request, self.template_name, {"posts": posts})