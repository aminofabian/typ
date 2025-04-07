from django.shortcuts import render
from .models import Trip

def index(request):
    return render(request, "trips/index.html", {
        "trips": Trip.objects.all()
    })

# Create your views here.
