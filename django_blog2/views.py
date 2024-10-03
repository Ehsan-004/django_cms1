from django.views.generic import TemplateView


class AboutUs(TemplateView):
    template_name = 'about_us.html'


class ContactUs(TemplateView):
    template_name = 'contact_us.html'
