from django.urls import path
from cbvapp import views

urlpatterns=[
    path('',views.Carlist.as_view(),name="cars"),
    path('<int:pk>',views.CompanyDetails.as_view())
]