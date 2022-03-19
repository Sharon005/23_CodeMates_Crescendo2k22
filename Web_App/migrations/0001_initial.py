# Generated by Django 3.2.7 on 2022-03-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('subject', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
