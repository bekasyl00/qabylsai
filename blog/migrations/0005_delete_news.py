# Generated by Django 4.1.1 on 2022-10-25 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_news_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='news',
        ),
    ]