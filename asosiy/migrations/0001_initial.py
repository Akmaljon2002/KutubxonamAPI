# Generated by Django 4.2 on 2023-04-25 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Audios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('rn', models.PositiveSmallIntegerField()),
                ('duration', models.DurationField()),
                ('size', models.CharField(max_length=5)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.topic')),
            ],
        ),
    ]
