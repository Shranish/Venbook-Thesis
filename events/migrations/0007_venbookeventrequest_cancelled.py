# Generated by Django 4.0.1 on 2022-06-14 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_canceledvenbookrequest_eventrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='venbookeventrequest',
            name='cancelled',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
