from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from mixins.ViewTitleMixin import ViewTitleMixin

from news.models import Post

# Create your views here.

class PostView(ViewTitleMixin, View):
    name = "post"
    title = "Myntsafnarafélag Íslands"
    
    template_name = 'news/post.html'
    def get(self, request, url=None):
        print(request)
        post = Post.objects.get(slug=url)
        return self.render(request, self.template_name, {"post": post})