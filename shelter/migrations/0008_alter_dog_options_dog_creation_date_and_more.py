# Generated by Django 5.0.3 on 2024-03-23 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0007_alter_breed_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dog',
            options={'ordering': ['breed', 'name'], 'verbose_name': 'Собака', 'verbose_name_plural': 'Собаки'},
        ),
        migrations.AddField(
            model_name='dog',
            name='creation_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='last_update_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='dogs'),
        ),
    ]