# Generated by Django 5.1.1 on 2024-09-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_post_intro_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='bg.png', upload_to='post_images/'),
        ),
    ]
