from django.db import models
from django.utils import timezone


#class defines object, Post is the models name and models.Model means its a django object
class Post (models.Model):
	
	#properties of Post are defined below
	author = models.ForeignKey('auth.User') #link to another model
	title = models.CharField(max_length=200) #limited num of characters
	text = models.TextField() #longtext
	created_date = models.DateTimeField(default=timezone.now) #date and time
	published_date = models.DateTimeField(blank=True, null=True)
	
	#method defined
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	
	def __str__(self):
		return self.title
