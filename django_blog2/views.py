from django.shortcuts import render
from django.views import View


class AboutUs(View):
    template_name = 'about_us.html'

    def get(self, request):
        return render(request, self.template_name)

class ContactUs(View):
    template_name = 'contact_us.html'

    def get(self, request):
        return render(request, self.template_name)