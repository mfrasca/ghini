# Generated by Django 2.2 on 2019-04-22 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_accession_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='accession',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='collection.Contact'),
        ),
    ]