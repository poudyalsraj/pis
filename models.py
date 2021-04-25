from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage
from datetime import datetime 
from django.utils import timezone

per_nonper_choices= (
	('permanent','permanent'), 
	('non_permanent', 'non_permanent')
	)


# main PIS database is here....  """

class Office(models.Model):

	name = models.CharField(max_length=255)
	ph_num= models.CharField(max_length = 20)
	email= models.CharField(max_length = 255)

	def __str__(self):
		return self.name


class Post(models.Model):
	name = models.CharField(max_length=255)
	level = models.CharField(max_length=255)
	salary= models.IntegerField(default=0)

	def __str__(self):
		return self.name



class Staff(models.Model):

	name = models.CharField(max_length=255)
	photo=models.ImageField(blank=True, upload_to = 'pis/')
	ph_num= models.CharField(max_length = 20)
	dob = models.DateField(default= timezone.now)

	post = models.ForeignKey(Post, on_delete=models.SET_NULL, null = True, blank=True)
	office = models.ForeignKey(Office, on_delete=models.SET_NULL, null = True, blank=True)

	def __str__(self):
		return self.name





class Darbandi (models.Model):

	office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null = True, blank=True)

	total_post = models.IntegerField(default=1)
	current_post = models.IntegerField(default=1)



	

class Address(models.Model):

	country = models.CharField(max_length=255)
	province = models.CharField(max_length=255)
	district = models.CharField(max_length=255)
	municipal = models.CharField(max_length=255)

	staff = models.OneToOneField(Staff, on_delete=models.CASCADE, null=True, blank=True)
	office = models.ForeignKey(Office, on_delete=models.CASCADE, null = True, blank=True)



	def __str__(self):
		return self.district


class Family(models.Model):

	mother_name = models.CharField(max_length = 255)
	father_name= models.CharField(max_length = 255)

	staff = models.OneToOneField(Staff, on_delete=models.CASCADE)

	def __str__(self):
		return self.father_name

class DesiredPerson (models.Model):

	name = models.CharField(max_length=255)
	relation= models.CharField(max_length=255)

	staff = models.OneToOneField(Staff, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
 





class Appointment (models.Model):

	staff = models.OneToOneField(Staff, on_delete=models.CASCADE )
	office = models.ForeignKey(Office, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	appointment_date = models.DateField(default= timezone.now)


	
class Service (models.Model):

	
	start_date = models.DateField(default= timezone.now)
	end_date = models.DateField(default= timezone.now)
	appointment_type = models.CharField(max_length=255, default='new')

	staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
	office = models.ForeignKey(Office, on_delete=models.CASCADE)

	def __str__(self):
		return self.appointment_type



class EducationalInfo (models.Model):

	
	Degree = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	institue_name = models.CharField(max_length=255)

	staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

	def __str__(self):
		return self.Degree





class LeaveInfo (models.Model):

	
	leave_type = models.CharField(max_length = 255)
	Leave_days = models.IntegerField(default = 0)
	staff = models.ForeignKey(Staff, on_delete = models.CASCADE)
	def __str__(self):
		return self.leave_type


class PunishmentInfo (models.Model):

	punishment_type = models.CharField(max_length=255)
	order_date = models.DateField(default= timezone.now)


	staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
	def __str__(self):
		return self.punishment_type



class Treatment (models.Model):

		amount = models.IntegerField (default=0)
		date = models.DateField (default=timezone.now)

		staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
		


class Document (models.Model):

	name = models.CharField(max_length=255)
	doc_file = models.FileField(upload_to = 'documents/', blank= True)

	staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
 


