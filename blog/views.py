from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import CreateView,View,ListView
from django.shortcuts import reverse
from django.urls import reverse_lazy
# Create your views here.

class BlogCreate(CreateView):
    model = Blog
    form_class = CreateBlog
    template_name = 'blog_create.html'
    success_url = reverse_lazy('view_blog')

class BlogView(ListView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = 'blog_list.html'


