# Generated by Django 3.2.4 on 2021-06-26 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_loans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loans',
            name='total_amount_to_pay',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
