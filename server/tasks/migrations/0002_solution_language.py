# Generated by Django 3.1.2 on 2020-10-31 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='language',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
