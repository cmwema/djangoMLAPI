from rest_framework import serializers
from .models import LoanApprovals


class LoanApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApprovals
        fields = "__all__"
