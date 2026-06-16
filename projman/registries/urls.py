from django.urls import path, include
from . import views

patterns_customers = [
	path('', views.customers_view, name="view"),
	path('create', views.create_customer_view, name="create"),
	path('bulk-delete', views.customers_bulk_delete, name="bulk-delete"),
	path('<int:id>/delete', views.customer_delete, name="delete"),
	path('<int:id>/edit', views.customer_edit, name="edit"),
]

patterns_executors = [
	path('', views.executors_view, name="view"),
	path('create', views.create_executor_view, name="create"),
	path('bulk-delete', views.executors_bulk_delete, name="bulk-delete"),
	path('<int:id>/delete', views.executor_delete, name="delete"),
	path('<int:id>/edit', views.executor_edit, name="edit"),
]

patterns_hardware = [
	path('', views.hardware_view, name="view"),
	path('create', views.create_device_view, name="create"),
	path('bulk-delete', views.hardware_bulk_delete, name="bulk-delete"),
	path('<int:id>/delete', views.device_delete, name="delete"),
	path('<int:id>/edit', views.device_edit, name="edit"),
]

patterns_staff = [
	path('', views.staff_view, name="view"),
	path('create', views.create_employee_view, name="create"),
	path('bulk-delete', views.staff_bulk_delete, name="bulk-delete"),
	path('<int:id>/delete', views.employee_delete, name="delete"),
	path('<int:id>/edit', views.employee_edit, name="edit"),
]

urlpatterns = [
	path('customers/', include((patterns_customers, 'customers'), namespace='customers')),
	path('executors/', include((patterns_executors, 'executors'), namespace='executors')),
	path('hardware/', include((patterns_hardware, 'hardware'), namespace='hardware')),
	path('staff/', include((patterns_staff, 'staff'), namespace='staff')),
]
