# Generated by Django 4.0.2 on 2022-02-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_redirect_link',
            field=models.URLField(default='#', max_length=255),
            preserve_default=False,
        ),
    ]