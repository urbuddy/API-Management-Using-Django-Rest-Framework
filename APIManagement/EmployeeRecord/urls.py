from django.urls import path
from .views import EmployeesDetails, EmployeeInfo

urlpatterns = [
    path('', EmployeesDetails.as_view(), name='emp'),
    path('<int:id>/', EmployeeInfo.as_view(), name='employee'),
]
