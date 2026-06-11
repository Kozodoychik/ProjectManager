from django.urls import path
from . import views

urlpatterns = [
	path('customers/', views.customers_view),
	path('executors/', views.executors_view),
	path('hardware/', views.hardware_view),
	path('staff/', views.staff_view)
]
