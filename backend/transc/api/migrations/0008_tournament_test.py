# Generated by Django 4.2.7 on 2024-02-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_delete_userstats'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='test',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
    ]