# Generated by Django 4.1.5 on 2023-01-31 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billshareapi', '0009_rename_bill_id_people_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billshareapi.paymenttype'),
        ),
    ]
