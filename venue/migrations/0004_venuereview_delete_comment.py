# Generated by Django 4.0.1 on 2022-07-04 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_account_address_alter_account_dob_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('venue', '0003_alter_comment_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('venue_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.venueaccount')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
