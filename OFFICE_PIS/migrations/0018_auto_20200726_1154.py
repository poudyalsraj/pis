# Generated by Django 3.0.7 on 2020-07-26 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OFFICE_PIS', '0017_auto_20200723_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.ImageField(blank=True, upload_to='pis'),
        ),
    ]
