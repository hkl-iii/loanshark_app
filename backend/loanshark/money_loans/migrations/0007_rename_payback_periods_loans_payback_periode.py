# Generated by Django 3.2.4 on 2021-07-06 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money_loans', '0006_rename_payback_periode_loans_payback_periods'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loans',
            old_name='payBack_periods',
            new_name='payBack_periode',
        ),
    ]