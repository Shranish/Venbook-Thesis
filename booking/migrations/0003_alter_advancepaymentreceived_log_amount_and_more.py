# Generated by Django 4.0.1 on 2022-06-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_advancepaymentreceived_advancepaymentreceived_log_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancepaymentreceived_log',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='advancepaymentsent_log',
            name='amount',
            field=models.FloatField(),
        ),
    ]