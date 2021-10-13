
from django.views.generic import TemplateView, FormView


class HomeView(TemplateView):
    template_name = "home.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class AboutView(TemplateView):
    template_name = "about.html"
