# Generated by Django 2.2.4 on 2019-08-23 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soldado', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='soldado',
            options={'permissions': {('is_dos', 'Usuario Dos')}},
        ),
        migrations.AlterField(
            model_name='cuerpo',
            name='id_cuerpo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='id_servicio',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]