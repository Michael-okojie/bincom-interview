from django.urls import path
from .views import IndividualPollingResult, PollingResultList, NewPollingUnit

urlpatterns = [
    path('', PollingResultList.as_view(), name='polling_results_list'),
    path('<int:pk>/', IndividualPollingResult.as_view(), name='individualpolling'),
    path('create/', NewPollingUnit.as_view(), name='new_polling_unit'),
    # path('list_total/', SumTotalLgaPolling.as_view(), name='total'),
]
