# Generated by Django 2.2 on 2019-04-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20190421_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accession',
            old_name='quantity_received',
            new_name='received_quantity',
        ),
        migrations.RenameField(
            model_name='accession',
            old_name='date_accessioned',
            new_name='accessioned_date',
        ),
        migrations.RenameField(
            model_name='accession',
            old_name='date_received',
            new_name='received_date',
        ),
        migrations.RenameField(
            model_name='accession',
            old_name='recvd_type',
            new_name='received_type',
        ),
    ]
