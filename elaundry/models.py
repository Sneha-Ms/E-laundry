from django.db import models
import hashlib

class Register(models.Model):
	name = models.CharField(max_length=200)
	rollNo = models.IntegerField()
	password = models.TextField()
	hostel = models.CharField(max_length=200)
	mobileNumber = models.IntegerField()
	mailId = models.TextField()

	def publish(self):
		self.password = hashlib.sha256(self.password).hexdigest()
		self.save()

	def __str__(self):
		return str(self.rollNo)