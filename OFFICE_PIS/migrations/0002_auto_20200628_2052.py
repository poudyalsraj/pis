# Generated by Django 3.0.7 on 2020-06-28 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OFFICE_PIS', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='office_id',
            new_name='office',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='staff_id',
            new_name='staff',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='office_id',
            new_name='office',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='darbandiinfo',
            old_name='office_id',
            new_name='office',
        ),
        migrations.RenameField(
            model_name='darbandiinfo',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='desiredperson',
            old_name='staff_id',
            new_name='staff',
        ),
        migrations.RenameField(
            model_name='educationalinfo',
            old_name='staff_id',
            new_name='staff',
        ),
        migrations.RenameField(
            model_name='family',
            old_name='staff_id',
            new_name='staff',
        ),
        migrations.RenameField(
            model_name='leaveinfo',
            old_name='staff_id',
            new_name='staff',
        ),
        migrations.RenameField(
            model_name='punishmentinfo',
            old_name='staff_id',
            new_name='staff',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='staff_id',
            new_name='staff',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='post_id',
            new_name='post',
        ),
    ]
