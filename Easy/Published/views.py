from django.shortcuts import render
from django.views.generic import TemplateView
from Membreship.models import Plans

# Create your views here.
class Published (TemplateView):
        template_name = 'published/published.html'
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['plans'] =  Plans.objects.filter(is_active=True)
            return context