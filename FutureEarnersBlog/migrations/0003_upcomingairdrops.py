# Generated by Django 5.0.2 on 2024-09-07 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FutureEarnersBlog', '0002_alter_socials_instagram_alter_socials_x_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='upcomingairdrops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('discription', models.CharField(max_length=170)),
                ('blog', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='FutureEarnersBlog.blog')),
            ],
        ),
    ]
