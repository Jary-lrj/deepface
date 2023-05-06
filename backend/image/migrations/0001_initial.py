# Generated by Django 3.2.18 on 2023-05-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('photo', models.ImageField(default='avatar.jpg', upload_to='photos')),
            ],
        ),
    ]
