# Generated by Django 3.0.7 on 2020-07-26 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OFFICE_PIS', '0020_document'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='document',
            new_name='doc_file',
        ),
    ]
