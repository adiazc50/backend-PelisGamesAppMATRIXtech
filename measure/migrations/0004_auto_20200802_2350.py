# Generated by Django 3.0.8 on 2020-08-03 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measure', '0003_prestamo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='idPrestamos',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]