from django.shortcuts import render, get_object_or_404, redirect
from meetings.models import Room
from .forms import RoomForm
# Create your views here.


def room_list(request):
	return render(request,
	              'rooms/room_list.html',
	              {'rooms': Room.objects.all()})


def detail(request, id):
	return render(request,
	              'rooms/detail.html',
	              {'room': get_object_or_404(Room, pk=id)})


def create(request):
	if request.method == "POST":
		form = RoomForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect('welcome')
	else:
		form = RoomForm()
		
	return render(request, 'rooms/create.html', {'form': form})


def update(request, id):
	room = get_object_or_404(Room, pk=id)
	
	form = RoomForm(request.POST, instance=room)
	
	if form.is_valid():
		form.save()
		return redirect('welcome')
	
	return render(request, 'rooms/update.html', {'form': form})


def delete(request, id):
	room = get_object_or_404(Room, pk=id)
	
	if request.method == 'POST':
		room.delete()
		return redirect('welcome')
	
	return render(request, 'rooms/delete.html', {'form': room})