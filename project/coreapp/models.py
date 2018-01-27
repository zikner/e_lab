from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Insurance(models.Model):
	""" Records Insurance companies that the hospital supports/allows transactions with."""

	name = models.CharField(max_length=100)

class LabTest(models.Model):
	""" Records lab tests that can be conducted """

	name = models.CharField(max_length=100)

class Laboratory(models.Model):
	""" Records laboratory names where lab test requests can be sent to """		

	name = models.CharField(max_length=100)

class Specimen(models.Model):
	""" Records specimen that accompany lab test requests """

	name = models.CharField(max_length=100)	

class Patient(models.Model):
	""" Patient details"""

	first_name = models.CharField(max_length=35)
	last_name = models.CharField(max_length=35)
	middle_name = models.CharField(max_length=35)
	email = models.EmailField()
	mobile = models.PhoneNumberField()
	date_of_birth = models.DateField()
	insurance_id = models.IntegerField()

	insurance = models.ForeignKey(Insurance, blank=True)

class LabRequest(models.Model):
	""" Records of lab requests made """

	 lab_test = models.ForeignKey(LabTest)
	 patient = models.ForeignKey(Patient)
	 date = models.DateTimeField(auto_now=True)
	 lab = models.ForeignKey(Laboratory, blank=True)
	 test_duration = models.TimeField()

class LabResult(models.Model):
	""" Records Lab results - not viewed yet and updated by a doctor """

	lab_request = models.ForeignKey(LabRequest) # the test conducted
	diagnosis = models.TextField(null=False, blank=False)
	date = models.DateField(auto_now_add=True) # date when the result was recorded
	lab = model.CharField(max_length=100)

class LabResultUpdated(models.Model):
	""" Records viewed and updated lab results, by the doctor """

	lab_request = models.ForeignKey(LabRequest)
	diagnosis = models.TextField(null=False, blank=False)
	visit_type = models.CharField(max_length=15)
	date = models.DateField(auto_now_add=True)
	lab = model.CharField(max_length=100)



