# Generated by Django 3.2.8 on 2021-10-30 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]