from django.urls import path
from . import views

urlpatterns = [
	path('customers/', views.customers_view),
	path('customers/<int:id>', views.customers_action),
	path('customers/create', views.create_customer_view),

	path('executors/', views.executors_view),
	path('executors/<int:id>', views.executors_action),
	path('executors/create', views.create_executor_view),

	path('hardware/', views.hardware_view),
	path('hardware/<int:id>', views.hardware_action),
	path('hardware/create', views.create_device_view),

	path('staff/', views.staff_view),
	path('staff/<int:id>', views.staff_action),
	path('staff/create', views.create_employee_view),
]
