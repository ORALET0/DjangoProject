from django.urls import path
from meetings.views import detail, create, update, delete

urlpatterns = [
	# Meetings
	path('<int:id>', detail, name='detail'),
	path('create', create, name='create'),
	path('update/<int:id>', update, name='update'),
	path('delete/<int:id>', delete, name='delete'),
]
