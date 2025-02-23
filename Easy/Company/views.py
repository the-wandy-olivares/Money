from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from .models import Company
from .forms import CompanyForm
# Create your views here.
class CompanyUpdate(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/company-update.html'

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('company:company-update' , kwargs={'pk': self.object.pk})
    