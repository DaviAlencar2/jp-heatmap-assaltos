# Generated by Django 5.1.7 on 2025-04-05 00:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Robbery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('street', models.CharField(blank=True, max_length=255)),
                ('number', models.CharField(blank=True, max_length=255)),
                ('latitude', models.CharField(blank=True, max_length=255)),
                ('longitude', models.CharField(blank=True, max_length=255)),
                ('type', models.CharField(choices=[('a', 'assalto'), ('f', 'furto')], default='a', max_length=1)),
                ('is_valid', models.BooleanField(default=False)),
                ('neighborhood', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='robberies', to='heatmap.neighborhood')),
            ],
        ),
    ]
