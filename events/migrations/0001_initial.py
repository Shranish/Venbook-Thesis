# Generated by Django 4.0.4 on 2022-06-02 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='OutEventInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=155)),
                ('event_date', models.DateField(max_length=155)),
                ('people', models.CharField(max_length=155)),
                ('event_details', models.TextField()),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.eventtype')),
                ('venue_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.venueaccount')),
            ],
        ),
        migrations.CreateModel(
            name='VenbookEventInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=155)),
                ('address', models.CharField(max_length=155)),
                ('email', models.EmailField(max_length=155)),
                ('phone', models.CharField(max_length=10)),
                ('event_name', models.CharField(max_length=155)),
                ('event_date', models.DateField(max_length=155)),
                ('people', models.CharField(max_length=155)),
                ('event_details', models.TextField()),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.eventtype')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('venue_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.venueaccount')),
            ],
        ),
        migrations.CreateModel(
            name='OutEventsUserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=155)),
                ('last_name', models.CharField(max_length=155)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('event_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.outeventinfo')),
            ],
        ),
    ]
