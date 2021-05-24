# Generated by Django 3.2.3 on 2021-05-23 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(default='', max_length=10)),
                ('firtName', models.CharField(default='', max_length=10)),
                ('lastName', models.CharField(default='', max_length=10)),
                ('avatar', models.ImageField(blank=True, upload_to=None)),
                ('status', models.BooleanField(default=True)),
                ('facebook', models.CharField(blank=True, default='', max_length=200)),
                ('github', models.CharField(blank=True, default='', max_length=200)),
                ('twitter', models.CharField(blank=True, default='', max_length=200)),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='g_emails', to='guser.guestuser')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='g_usernames', to='guser.guestuser')),
            ],
        ),
    ]
