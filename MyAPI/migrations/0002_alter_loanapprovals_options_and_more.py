# Generated by Django 5.0.3 on 2024-03-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loanapprovals',
            options={'verbose_name_plural': 'LoanApprovals'},
        ),
        migrations.AlterField(
            model_name='loanapprovals',
            name='applicant_income',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loanapprovals',
            name='coapplicant_income',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loanapprovals',
            name='credit_history',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loanapprovals',
            name='dependants',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loanapprovals',
            name='loan_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loanapprovals',
            name='loan_term',
            field=models.IntegerField(default=0),
        ),
    ]
