# Generated by Django 4.2.1 on 2023-05-22 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ParkingApp', '0002_alter_parkingplace_auto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auto',
            options={'ordering': ['brand', 'model'], 'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterModelOptions(
            name='parkingplace',
            options={'ordering': ['price'], 'verbose_name': 'Parking place', 'verbose_name_plural': 'Parking places'},
        ),
        migrations.AddField(
            model_name='client',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ParkingApp.parkingplace'),
        ),
        migrations.AlterField(
            model_name='client',
            name='checks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ParkingApp.check'),
        ),
    ]