import os
import numpy as np
import pandas as pd
from keras.models import load_model
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import LoanApprovalSerializer
from .models import LoanApprovals

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "loan_model.keras")
model = load_model(model_path)


class LoanApprovalsView(generics.GenericAPIView):
    serializer_class = LoanApprovalSerializer
    permission_classes = [IsAuthenticated]  # Example permission, adjust as needed

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            column_mapping = {
                "applicant_income": "ApplicantIncome",
                "coapplicant_income": "CoapplicantIncome",
                "loan_amount": "LoanAmount",
                "loan_term": "Loan_Amount_Term",
                "credit_history": "Credit_History",
                "gender": "Gender",
                "married": "Married",
                "graduate": "Education",
                "self_employed": "Self_Employed",
                "area": "Property_Area",
                "dependants": "Dependents",
            }
            df = pd.DataFrame([data])
            df = df.rename(columns=column_mapping)
            columns_order = [
                "Gender",
                "Married",
                "Dependents",
                "Education",
                "Self_Employed",
                "ApplicantIncome",
                "CoapplicantIncome",
                "LoanAmount",
                "Loan_Amount_Term",
                "Credit_History",
                "Property_Area",
            ]
            df = df[columns_order]

            categorical_columns = [
                "Gender",
                "Married",
                "Education",
                "Self_Employed",
                "Property_Area",
            ]
            df = pd.get_dummies(df, columns=categorical_columns, dummy_na=True)
            if "Married_yes" in df.columns:
                if all(df["Married_yes"]):
                    df = df.rename(columns={"Married_nan": "Married_no"})
                else:
                    df = df.rename(columns={"Married_nan": "Married_yes"})
            if "Education_yes" in df.columns:
                if all(df["Education_yes"]):
                    df = df.rename(columns={"Education_nan": "Education_no"})
                else:
                    df = df.rename(columns={"Education_nan": "Education_yes"})
            if "Self_Employed_yes" in df.columns:
                if all(df["Self_Employed_yes"]):
                    df = df.rename(columns={"Self_Employed_nan": "Self_Employed_no"})
                else:
                    df = df.rename(columns={"Self_Employed_nan": "Self_Employed_yes"})
            if "Gender_male" in df.columns:
                if all(df["Gender_male"]):
                    df = df.rename(columns={"Gender_nan": "Gender_female"})
                else:
                    df = df.rename(columns={"Gender_nan": "Gender_male"})
            if "Property_Area_Urban" in df.columns:
                if all(df["Property_Area_Urban"]):
                    df = df.rename(columns={"Property_Area_nan": "Property_Area_Rural"})
                    df['Property_Area_Semiurban'] = False
                else:
                    df = df.rename(columns={"Property_Area_nan": "Property_Area_Urban"})
                    df['Property_Area_Semiurban'] = False
            if "Property_Area_Rural" in df.columns:
                if all(df["Property_Area_Rural"]):
                    df = df.rename(columns={"Property_Area_nan": "Property_Area_Semiurban"})
                    df['Property_Area_Urban'] = False
                else:
                    df = df.rename(columns={"Property_Area_nan": "Property_Area_Rural"})
                    df['Property_Area_Urban'] = False
            if "Property_Area_Semiurban" in df.columns:
                if all(df["Property_Area_Semiurban"]):
                    df = df.rename(columns={"Property_Area_nan": "Property_Area_Rural"})
                    df['Property_Area_Urban'] = False
                else:
                    df = df.rename(columns={"Property_Area_nan": "Property_Area_Semiurban"})
                    df['Property_Area_Urban'] = False
            print(df.columns)
            return Response(df.columns)
        except ValueError as e:
            return Response(str(e), status=400)
