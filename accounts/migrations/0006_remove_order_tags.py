# Generated by Django 2.0.7 on 2021-06-09 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210609_0630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
    ]