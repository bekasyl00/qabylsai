# Generated by Django 4.1.1 on 2022-10-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_statia_text_statia_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='statia',
            name='views',
            field=models.IntegerField(default=1, verbose_name='prosmotr'),
        ),
        migrations.AlterField(
            model_name='statia',
            name='title',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='aty'),
        ),
    ]
