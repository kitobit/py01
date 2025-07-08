from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Articles

def news_home(request):
	news = Articles.objects.all().order_by('-date')
	return render(request, 'news/news_home.html',{'news':news})

