# Generated by Django 5.0.2 on 2024-09-07 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FutureEarnersBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socials',
            name='Instagram',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterField(
            model_name='socials',
            name='X',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterField(
            model_name='socials',
            name='You_tube',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterField(
            model_name='socials',
            name='telegram',
            field=models.URLField(max_length=300),
        ),
    ]
