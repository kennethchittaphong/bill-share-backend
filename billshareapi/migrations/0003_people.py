# Generated by Django 4.1.5 on 2023-01-27 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billshareapi', '0002_bill_split_amount_bill_total_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('due_date', models.DateField(max_length=55)),
                ('amount', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=55)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billshareapi.user')),
            ],
        ),
    ]