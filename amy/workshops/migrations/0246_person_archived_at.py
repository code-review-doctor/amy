# Generated by Django 2.2.17 on 2021-05-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0245_membership_extensions'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='archived_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]