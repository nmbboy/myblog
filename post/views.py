from django.shortcuts import render
from .models import Post
from django.views.generic import *


class IndexView(ListView):
    model = Post
    queryset = Post.objects.filter(isdelete=False).order_by("-createdate")
    template_name = 'index.html'
    context_object_name = 'Postlist'
