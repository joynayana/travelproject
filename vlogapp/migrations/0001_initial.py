# Generated by Django 3.2.12 on 2022-03-18 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='current',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='vlog pictures')),
                ('category', models.TextField()),
                ('desc', models.TextField()),
                ('month', models.CharField(max_length=20)),
                ('day', models.IntegerField()),
            ],
        ),
    ]
