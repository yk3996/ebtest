from django.shortcuts import render
from .models import Portfolio

# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'portfolios':portfolios})