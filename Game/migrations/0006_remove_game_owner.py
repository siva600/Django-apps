# Generated by Django 2.2 on 2019-04-11 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0005_game_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='owner',
        ),
    ]
