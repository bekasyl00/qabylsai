# Generated by Django 4.1.1 on 2023-02-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_statia_poto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statia',
            name='poto',
            field=models.ImageField(default='default.png', upload_to='news_images', verbose_name='фото'),
        ),
    ]
