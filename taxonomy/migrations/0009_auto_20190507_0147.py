# Generated by Django 2.2 on 2019-05-07 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0008_auto_20190430_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='show_as',
            field=models.CharField(default='<i>.epithet</i> sp.', max_length=48),
        ),
    ]
