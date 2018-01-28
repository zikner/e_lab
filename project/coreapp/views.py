from django.shortcuts import render
from django.views import View
from .forms import PatientSearchForm
from . import models
# Create your views here.

class SearchPatient(View):

	def get(self, request):

		form = PatientSearchForm()
		return render(request, 'coreapp/patient_search_form.html', {'form': form})

	def post(self, request):
		
		form = PatientSearchForm(request.POST)

		if form.is_valid():

			first_name = form.cleaned_data['first_name']
			mobile = form.cleaned_data.get('mobile')
			member_id = form.cleaned_data.get('member_id')

			if mobile:
				query_set = models.Patient.objects.filter(first_name=first_name, mobile=mobile)

			elif member_id:
				query_set = models.Patient.objects.filter(first_name=first_name, mobile=mobile)

			else:
				query_set = models.Patient.objects.filter(first_name=first_name)
			
			return render(request, 'coreapp/patient_search_results.html', {'query_set': query_set})

		
		else:
			return render(request, 'coreapp/patient_search_form.html', {'form': form})


