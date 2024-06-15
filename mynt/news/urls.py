from django.urls import path

from django.conf.urls import include

from .views import index, specific_post

urlpatterns = [
    path("", index.Index.as_view(), name="index"),
    path("post/<url>", specific_post.PostView.as_view(), name="post"),

]