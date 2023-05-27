# Generated by Django 4.2.1 on 2023-05-27 13:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ParkingApp', '0003_alter_auto_options_alter_parkingplace_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='checks',
        ),
        migrations.AddField(
            model_name='check',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ParkingApp.client'),
        ),
        migrations.AlterField(
            model_name='client',
            name='number',
            field=models.CharField(default='+375 (29) xxx-xx-xx', max_length=20, validators=[django.core.validators.RegexValidator(regex='^\\+375 \\(29\\) \\d{3}-\\d{2}-\\d{2}$')]),
        ),
    ]
