# Generated by Django 4.2 on 2023-04-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dht',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.TextField(max_length=64)),
                ('hum', models.TextField(max_length=46)),
            ],
        ),
    ]