# Generated by Django 2.1.4 on 2018-12-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Komentarze',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tresc', models.TextField()),
                ('nickname', models.CharField(max_length=200, unique=True)),
                ('tytul', models.CharField(max_length=200, unique=True)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('data', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Komentarze',
            },
        ),
    ]