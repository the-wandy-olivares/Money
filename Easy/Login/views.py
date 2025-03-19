from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


class Login(TemplateView):
      template_name = 'login/login.html'

      def post(self, request, *args, **kwargs):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                  login(request, user)
                  return HttpResponseRedirect('/')  # Redirect to a dashboard or home page
            return render(request, self.template_name, {'error': 'Invalid credentials'})
