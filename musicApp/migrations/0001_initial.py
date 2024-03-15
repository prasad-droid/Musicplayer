# Generated by Django 4.2.11 on 2024-03-15 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('liked_songs', models.JSONField(null=False)),
                ('playlists', models.JSONField(null=False)),
            ],
        ),
    ]
