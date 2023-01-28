# Generated by Django 4.1.5 on 2023-01-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0007_alter_player_current_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='current_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]