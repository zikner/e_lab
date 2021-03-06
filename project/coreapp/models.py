from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Insurance(models.Model):
	""" Records Insurance companies that the hospital supports/allows transactions with."""

	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'insurance'


class LabTest(models.Model):
	""" Records lab tests that can be conducted """

	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Laboratory(models.Model):
	""" Records laboratory names where lab test requests can be sent to """		

	name = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = 'laboratories'

	def __str__(self):
		return self.name	

class Specimen(models.Model):
	""" Records specimen that accompany lab test requests """

	name = models.CharField(max_length=100)	

	def __str__(self):
		return self.name

class Patient(models.Model):
	""" Patient details"""

	first_name = models.CharField(max_length=35, verbose_name='first name')
	last_name = models.CharField(max_length=35)
	middle_name = models.CharField(max_length=35)
	email = models.EmailField()
	mobile = PhoneNumberField()
	date_of_birth = models.DateField()
	member_id = models.IntegerField(verbose_name='insurance member id', blank=True)

	insurance = models.ForeignKey(Insurance, models.SET_NULL, null=True, verbose_name='insurance company')

	def __str__(self):
		return self.middle_name

class LabRequest(models.Model):
	""" Records of lab requests made """

	lab_test = models.ForeignKey(LabTest, models.PROTECT)
	patient = models.ForeignKey(Patient, models.PROTECT)
	date = models.DateTimeField(auto_now=True)
	lab = models.ForeignKey(Laboratory, models.SET_NULL,null=True)
	test_duration = models.TimeField()

	def __str__(self):
		return "{} request for patient by name {} {}".format(self.lab_test, self.patient.first_name, self.patient.middle_name)   

class LabResult(models.Model):
	""" Records Lab results - not viewed yet and updated by a doctor """

	lab_request = models.ForeignKey(LabRequest, models.PROTECT) # the test conducted
	diagnosis = models.TextField(null=False, blank=False)
	date = models.DateField(auto_now_add=True) # date when the result was recorded
	lab = models.ForeignKey(Laboratory, models.SET_NULL, null=True)

	def __str__(self):
		return '[possible diagnosis]: ' + self.diagnosis

class LabResultUpdated(models.Model):
	""" Records viewed and updated lab results, by the doctor """

	lab_request = models.ForeignKey(LabRequest, models.PROTECT)
	diagnosis = models.TextField(null=False, blank=False)
	visit_type = models.CharField(max_length=15)
	date = models.DateField(auto_now_add=True)
	lab = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = 'lab results updated'


	def __str__(self):
		return 'diagnosis: ' + self.diagnosis	
