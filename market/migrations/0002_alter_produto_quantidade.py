# Generated by Django 4.2.16 on 2024-11-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(),
        ),
    ]