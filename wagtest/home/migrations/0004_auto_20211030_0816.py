# Generated by Django 3.2.8 on 2021-10-30 05:16

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='rtfbody',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Подзаголовок'),
        ),
    ]
