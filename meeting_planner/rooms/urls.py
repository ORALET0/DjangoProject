
from django.urls import path
from rooms.views import room_list, detail, create, update, delete


urlpatterns = [
	path('rooms', room_list, name='rooms'),
	path('<int:id>', detail, name='detail'),
	path('create', create, name='create'),
	path('update/<int:id>', update, name='update'),
	path('delete/<int:id>', delete, name='delete'),
]