# Generated by Django 4.1.5 on 2023-01-28 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billshareapi', '0004_bill_bill_id_people_bill_id_alter_bill_split_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='user',
        ),
    ]