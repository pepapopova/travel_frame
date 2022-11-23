# Generated by Django 4.1.3 on 2022-11-22 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_photos', '0004_remove_travelphoto_tagged_users_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0002_travelphotocomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelphotolike',
            name='travel_photo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='travel_photos.travelphoto'),
        ),
        migrations.AlterField(
            model_name='travelphotolike',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]