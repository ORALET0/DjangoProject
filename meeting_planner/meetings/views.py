from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room
from .forms import MeetingForm


# Create your views here.


def detail(request, id):
	meeting = get_object_or_404(Meeting, pk=id)
	
	return render(request,
	              'meetings/detail.html',
	              {'meeting': meeting})


# forms.py dosyası içerisinde MeetingForm hazırlamadan hali hazırda bulunan models içerisinde ki Meeting sınıfı kullanılarak MeetingForm oluşturulabilinirdi.
# django bunu yaparken size soyutlamada çaktırmadan anlatığım factory design pattern kullanarak Meeting modelinden form yaratır.
# MeetingForm = modelform_factory(Meeting, exclude=[])
# ama biz bunu kullanamayacağız çünkü MeetingForm customize ederek biz oluşturduk.


def create(request):
	if request.method == 'POST':
		form = MeetingForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect('welcome')
	else:
		form = MeetingForm()
	
	return render(request,
	              'meetings/create.html',
	              {'form': form})


def update(request, id):
	meeting = get_object_or_404(Meeting, pk=id)
	form = MeetingForm(request.POST, instance=meeting)
	
	if form.is_valid():
		form.save()
		return redirect('welcome')
	
	return render(request, 'meetings/update.html', {'form': form})
	
	
def delete(request, id):
	meeting = get_object_or_404(Meeting, pk=id)
	
	if request.method == 'POST':
		meeting.delete()
		return redirect('welcome')
	
	return render(request, 'meetings/delete.html', {'form': meeting})
	