import datetime
from django.views.generic import TemplateView


# Create your views here.

class Home(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = datetime.datetime.now().strftime("%H:%M:%S")
        return context
