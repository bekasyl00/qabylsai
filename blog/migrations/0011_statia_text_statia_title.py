# Generated by Django 4.1.1 on 2022-10-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_statia_text_remove_statia_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='statia',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='angime'),
        ),
        migrations.AddField(
            model_name='statia',
            name='title',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='aty'),
        ),
    ]
