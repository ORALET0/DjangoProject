import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting


# Create your views here.


def welcome(request):
	return render(request,
	              'website/welcome.html',
	              {
		              'message': 'Welcome to the Meeting Planer App',
		              'num_meeting': Meeting.objects.count(),
		              'meetings': Meeting.objects.all()
				  })


def about(request):
	return HttpResponse('Copyright Tyson Solution.')


def date(request):
	return HttpResponse(datetime.datetime.now())