# Generated by Django 3.2 on 2021-04-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_img', models.ImageField(upload_to='images/')),
                ('service_name', models.CharField(max_length=100)),
                ('service_description', models.CharField(max_length=250)),
            ],
        ),
    ]
