from django.forms import ModelForm
from .models import Patient

class PatientSearchForm(ModelForm):

	class Meta:
		model = Patient
		fields = ['first_name', 'mobile', 'member_id']

