from django.shortcuts import render
from django.views.generic import TemplateView


class Inversion(TemplateView):
      template_name = "inversion/inversion.html"
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context
      
      def get(self, request, *args, **kwargs):
            context = self.get_context_data(**kwargs)
            return render(request, self.template_name, context)

# Create your views here.
