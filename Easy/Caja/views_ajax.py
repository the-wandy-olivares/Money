from datetime import datetime
from django.http import JsonResponse
from . import models
from django.db.models import Q



def SearchMove(request):
      d = request.GET.get('search', '').strip()
      data = []
      if d:
            data = models.Movements.objects.filter(description__icontains=d).values('id', 'description', 'description', 'date', 'mount', 'type')
      return JsonResponse(list(data), safe=False)