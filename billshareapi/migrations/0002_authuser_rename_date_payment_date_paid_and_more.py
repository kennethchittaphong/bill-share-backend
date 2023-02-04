# Generated by Django 4.1.5 on 2023-02-04 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billshareapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('is_staff', models.CharField(max_length=50)),
                ('is_active', models.CharField(max_length=50)),
                ('last_login', models.DateTimeField(max_length=50)),
                ('is_superuser', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='date',
            new_name='date_paid',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='name',
            new_name='label',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='uid',
        ),
        migrations.AddField(
            model_name='bill',
            name='split_amount',
            field=models.JSONField(default=''),
        ),
        migrations.AddField(
            model_name='bill',
            name='total_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='amount_paid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='bill',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='billshareapi.bill'),
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('due_date', models.DateField(max_length=55)),
                ('amount', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=55)),
                ('bill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='billshareapi.bill')),
            ],
        ),
    ]