# Generated by Django 2.1.1 on 2018-09-24 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20, unique=True)),
                ('lastname', models.CharField(max_length=15)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(max_length=200)),
            ],
        ),
    ]
