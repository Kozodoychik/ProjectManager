from django.urls import path, include
from . import views

patterns_customers = [
	path('', views.customers_view, name="view"),
	path('delete', views.customers_delete, name="delete"),
	path('create', views.create_customer_view, name="create"),
	path('edit/<int:id>', views.customers_edit, name="edit"),
]

patterns_executors = [
	path('', views.executors_view, name="view"),
	path('delete', views.executors_delete, name="delete"),
	path('create', views.create_executor_view, name="create"),
	path('edit/<int:id>', views.executors_edit, name="edit"),
]

patterns_hardware = [
	path('', views.hardware_view, name="view"),
	path('delete', views.hardware_delete, name="delete"),
	path('create', views.create_device_view, name="create"),
	path('edit/<int:id>', views.hardware_edit, name="edit"),
]

patterns_staff = [
	path('', views.staff_view, name="view"),
	path('delete', views.staff_delete, name="delete"),
	path('create', views.create_employee_view, name="create"),
	path('edit/<int:id>', views.staff_edit, name="edit"),
]

urlpatterns = [
	path('customers/', include((patterns_customers, 'customers'), namespace='customers')),
	path('executors/', include((patterns_executors, 'executors'), namespace='executors')),
	path('hardware/', include((patterns_hardware, 'hardware'), namespace='hardware')),
	path('staff/', include((patterns_staff, 'staff'), namespace='staff')),
]
