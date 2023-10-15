# Generated by Django 3.2.21 on 2023-10-15 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='original_bag',
        ),
        migrations.RemoveField(
            model_name='order',
            name='stripe_pid',
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
