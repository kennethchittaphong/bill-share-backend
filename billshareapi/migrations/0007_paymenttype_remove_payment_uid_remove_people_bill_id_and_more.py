# Generated by Django 4.1.5 on 2023-01-30 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billshareapi', '0006_remove_bill_bill_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=55)),
            ],
        ),
        migrations.RemoveField(
            model_name='payment',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='people',
            name='bill_id',
        ),
        migrations.AddField(
            model_name='payment',
            name='bill',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='billshareapi.bill'),
        ),
        migrations.AddField(
            model_name='payment',
            name='total',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='bill',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='billshareapi.bill'),
        ),
    ]
