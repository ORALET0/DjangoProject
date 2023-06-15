from datetime import time
from enum import Enum
from django.db import models

# Seed Data yap.


class Status(Enum):
	Active = 1
	Modified = 2
	Passive = 3


class Page(models.Model):
	title = models.CharField(max_length=250, db_index=True)
	content = models.CharField(max_length=250)
	slug = models.SlugField(max_length=255)
	
	def __str__(self):
		return f'{self.title}'
	
	class Meta:
		verbose_name_plural = 'pages'


class Room(models.Model):
	name = models.CharField(max_length=50)
	floor = models.CharField(max_length=50)
	room_number = models.IntegerField()
	status = models.IntegerField()
	slug = models.SlugField(max_length=255, db_index=True)
	price = models.DecimalField(max_digits=4, decimal_places=2)
	
	def __str__(self):
		return f'{self.name}: room ' \
		       f'{self.room_number} on floor ' \
		       f'{self.floor}'
	
	class Meta:
		verbose_name_plural = 'rooms'
	
	
class Meeting(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateField()
	start_time = models.TimeField(default=time(9))
	duration = models.IntegerField(default=1)
	slug = models.SlugField(max_length=255, db_index=True)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	
	def __str__(self):
		return f'{self.title} at ' \
		       f'{self.start_time} on ' \
		       f'{self.date}'
	
	class Meta:
		verbose_name_plural = 'meetings'
	
	
class AppUser(models.Model):
	full_name = models.CharField(max_length=200)
	user_name = models.CharField(max_length=200, unique=True, db_index=True)
	password = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images/')
	
	def __str__(self):
		return f'{self.full_name}'
		
	class Meta:
		verbose_name_plural = 'appusers'
	