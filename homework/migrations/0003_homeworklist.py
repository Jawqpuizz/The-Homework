# Generated by Django 3.0.4 on 2020-08-23 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_auto_20200822_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeworkList',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('hw_desc', models.CharField(max_length=100)),
                ('hw_file', models.CharField(max_length=255)),
                ('creator', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'homeworks',
            },
        ),
    ]
