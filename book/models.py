from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import *

# Create your models here.

class Pin(models.Model):
	
	user = models.OneToOneField(User, primary_key=True)
	user_pin = models.CharField(max_length=4)		

	def __unicode__(self):
		return self.user_pin

class PhoneNumber(models.Model):
	user = models.ForeignKey(User)
	#first_name = models.CharField(max_length=30, blank=False)
	#last_name = models.CharField(max_length=30, blank=False)
	phone = models.IntegerField()

	def __unicode__(self):
		return unicode(self.user)

class Email_Add(models.Model):
	user = models.ForeignKey(User)
	email_address = models.CharField(max_length=30)

	def __unicode__(self):
		return self.email_address

class SocialNetwork(models.Model):
	user = models.ForeignKey(User)
	facebook = models.URLField(blank=True)
	twitter = models.URLField(blank=True)

	def __unicode__(self):
		return self.user.username

class Website(models.Model):
	user = models.ForeignKey(User)
	web_site = models.URLField(blank=True)
	blog = models.URLField(blank=True)

	def __unicode__(self):
		return self.user.username

class MyContacts(models.Model):
	user = models.ForeignKey(User)
	contact_id = models.IntegerField()

	def __unicode__(self):
		return self.user.username
