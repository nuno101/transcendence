# Generated by Django 4.2.7 on 2024-02-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_tournament_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tournaments',
            field=models.ManyToManyField(blank=True, related_name='participants', to='api.tournament'),
        ),
    ]
