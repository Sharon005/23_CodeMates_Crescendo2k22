# Generated by Django 3.2.7 on 2022-03-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_App', '0003_rename_subject_contactus_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('desc', models.TextField(max_length=3000, null=True)),
                ('slug', models.CharField(max_length=48)),
            ],
        ),
        migrations.RenameModel(
            old_name='ContactUS',
            new_name='Adoption',
        ),
    ]