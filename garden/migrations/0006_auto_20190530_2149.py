# Generated by Django 2.2 on 2019-05-30 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0005_plantimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantimage',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='garden.Plant'),
        ),
    ]
