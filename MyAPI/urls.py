from django.urls import path
from .views import LoanApprovalsView

urlpatterns = [path("", LoanApprovalsView.as_view())]
