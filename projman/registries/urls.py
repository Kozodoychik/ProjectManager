from django.urls import path
from . import views

urlpatterns = [
	path('customers/', views.customers_view),
	path('customers/delete', views.customers_delete),
	path('customers/edit/<int:id>', views.customers_edit),
	path('customers/create', views.create_customer_view),

	path('executors/', views.executors_view),
	path('executors/delete', views.executors_delete),
	path('executors/edit/<int:id>', views.executors_edit),
	path('executors/create', views.create_executor_view),

	path('hardware/', views.hardware_view),
	path('hardware/delete', views.hardware_delete),
	path('hardware/edit/<int:id>', views.hardware_edit),
	path('hardware/create', views.create_device_view),

	path('staff/', views.staff_view),
	path('staff/delete', views.staff_delete),
	path('staff/edit/<int:id>', views.staff_edit),
	path('staff/create', views.create_employee_view),
]
