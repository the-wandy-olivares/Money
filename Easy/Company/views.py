from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView

# Create your views here.
class  Company(TemplateView):
    template_name = "company/company.html"