# Desc: URL patterns for the app
from django.urls import path
from .views import Agenda

app_name = "agenda"
urlpatterns = [
      path('', Agenda.as_view(), name='agenda'),
]