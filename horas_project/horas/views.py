from django.shortcuts import render
from django.utils import timezone
from .models import Horas_Model

def horas_list(request):
        model = Horas_Model.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'horas/horas_list.html', {'horas': model})
