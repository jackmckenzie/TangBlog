from django.shortcuts import render
from django.views import generic
from . import models

class BlogIndex(generic.ListView):
    queryset = models.Post.objects.published()
    template_name = 'blog/home.html'
    paginate_by = 2

class BlogDetail(generic.DetailView):
    model = models.Post
    template_name = "blog/post.html"


# Create your views here.
