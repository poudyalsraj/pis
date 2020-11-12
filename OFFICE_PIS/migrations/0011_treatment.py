# Generated by Django 3.0.7 on 2020-07-19 06:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('OFFICE_PIS', '0010_auto_20200703_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]