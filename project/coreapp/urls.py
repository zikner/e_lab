from django.urls import path
from . import views


app_name = 'coreapp'

urlpatterns = [
    path('search-patient/', views.SearchPatient.as_view(), name='search-patient')
]
