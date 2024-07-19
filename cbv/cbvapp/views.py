from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from cbvapp.models import Company

# Create your views here.
# class Myclass(View):
#     def get(self,request):
#         return HttpResponse("Class Based Views CBV")



class indexView(TemplateView):
    template_name ="index.html"

class Carlist(ListView):
    model = Company
    # context_object_name = "companies"

class CompanyDetails(DetailView):
    model = Company
    context_object_name='company_details'
