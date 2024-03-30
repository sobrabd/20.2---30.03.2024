# Generated by Django 5.0.3 on 2024-03-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('breed', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='dogs')),
                ('birth_date', models.DateField()),
            ],
        ),
    ]