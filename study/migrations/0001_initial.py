# Generated by Django 5.1 on 2024-10-08 01:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('study_id', models.AutoField(primary_key=True, serialize=False)),
                ('study_name', models.CharField(max_length=255)),
                ('study_description', models.TextField()),
                ('study_phase', models.CharField(choices=[('Phase I', 'Phase I'), ('Phase II', 'Phase II'), ('Phase III', 'Phase III'), ('Phase IV', 'Phase IV')], max_length=10)),
                ('sponsor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.sponsor')),
            ],
        ),
    ]
