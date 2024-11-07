# Generated by Django 5.1.3 on 2024-11-06 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='id_vehiculo',
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='categoria',
            field=models.CharField(choices=[('PARTICULAR', 'Particular'), ('TRANSPORTE', 'Transporte'), ('CARGA', 'Carga')], default='Particular', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(choices=[('FIAT', 'Fiat'), ('CHEVROLET', 'Chevrolet'), ('FORD', 'Ford'), ('TOYOTA', 'Toyota')], default='Ford', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='precio',
            field=models.PositiveSmallIntegerField(),
        ),
    ]