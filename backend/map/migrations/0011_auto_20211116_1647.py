# Generated by Django 3.1.8 on 2021-11-16 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='map',
            old_name='med_point_id',
            new_name='med_point',
        ),
        migrations.AlterField(
            model_name='map',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='medpoint',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]