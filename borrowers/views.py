from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView

# Create your views here.


class LandingPageView(TemplateView):
    template_name = "index.html"


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutUsView(TemplateView):
    template_name = "about_us.html"