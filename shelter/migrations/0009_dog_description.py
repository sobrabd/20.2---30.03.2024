# Generated by Django 5.0.3 on 2024-03-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0008_alter_dog_options_dog_creation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
