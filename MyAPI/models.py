from django.db import models

GENDER_CHOICES = (
    ("male", "male"),
    ("female", "female"),
)
MARRIED_CHOICES = (("yes", "yes"), ("no", "no"))
GRADUATE_CHOICES = (("graduate", "graduated"), ("not_graduate", "not_graduate"))
SELF_EMPLOYED_CHOICES = (("yes", "yes"), ("no", "no"))
PROPERTY_CHOICES = (
    ("rural", "rural"),
    ("semiurban", "semiurban"),
    ("urban", "urban"),
)


class LoanApprovals(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dependants = models.IntegerField(default=0)
    applicant_income = models.IntegerField(default=0)
    coapplicant_income = models.IntegerField(default=0)
    loan_amount = models.IntegerField(default=0)
    loan_term = models.IntegerField(default=0)
    credit_history = models.IntegerField(default=0)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
    graduate = models.CharField(max_length=15, choices=GRADUATE_CHOICES)
    self_employed = models.CharField(max_length=15, choices=SELF_EMPLOYED_CHOICES)
    area = models.CharField(max_length=15, choices=PROPERTY_CHOICES)

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        verbose_name_plural = "LoanApprovals"
