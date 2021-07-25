from .views import ExpenseSummaryStats, IncomeSummaryStats
from django.urls import path

urlpatterns = [
    path('expense_category_data', ExpenseSummaryStats.as_view(),
         name='expense_category_data'),
    path('income_source_data', IncomeSummaryStats.as_view(),
         name='income_source_data')
]
