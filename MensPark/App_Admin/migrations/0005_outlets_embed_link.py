# Generated by Django 4.0.3 on 2022-04-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Admin', '0004_outlets'),
    ]

    operations = [
        migrations.AddField(
            model_name='outlets',
            name='embed_link',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
