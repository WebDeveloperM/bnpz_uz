# Generated by Django 5.0.6 on 2024-07-01 05:27

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leadership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250)),
                ('career', models.CharField(max_length=250)),
                ('reception_time', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('activity', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
