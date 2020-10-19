# Generated by Django 3.1 on 2020-08-24 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30, unique=True)),
                ('spwd', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 't_stu',
            },
        ),
    ]
