from django.views.generic import  TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from Client import models
from Credit import models
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect


class Dashboard(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cont_clients'] = models.Client.objects.all().count()
        context['count_credits'] = models.Credit.objects.all().count()
        return context
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login:login')
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
    

def Logout(request):
        logout(request)
        return HttpResponseRedirect('/')
