from django.views.generic import TemplateView
import datetime
# Create your views here.

class Info(TemplateView):
    template_name = 'info/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = datetime.datetime.now().strftime("%H:%M:%S")
        return context
