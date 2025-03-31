from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from Company.models import Company, More
from Membreship.models import Membership, Plans
from django.utils import timezone

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


class CreateUserCompany(TemplateView):
      template_name = 'login/create-user-company.html'

      def post(self, request, *args, **kwargs):

            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.create(username=username, first_name=username)

            user.set_password(password)  # Encripta la contraseña
            user.save()
            company = Company.objects.create(
                  user = user,
                  name = request.POST.get('name_company'),
                  logo = request.FILES.get('id_img_portada'),
                  img_portada = request.FILES.get('id_img_portada')
            )
            More.objects.create(
                  user = user,
                  role='Administrador',
                  company = company,
                  img = request.FILES.get('id_img_portada')
            )
            Membership.objects.create(
                  user= user,
                  plan = Plans.objects.get(is_active=True).first(),

            )
            user_ready = authenticate(request, username=username, password=password)
            if user_ready is not None:
                  login(request, user)
                  return HttpResponseRedirect('/')  # Redirect to a dashboard or home page
            return render(request, self.template_name, {'error': 'Invalid credentials'})
