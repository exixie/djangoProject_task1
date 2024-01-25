from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, TemplateView


class BlogList(ListView):
    model = Post
    template_name = 'home.html'

class BlogDateDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
