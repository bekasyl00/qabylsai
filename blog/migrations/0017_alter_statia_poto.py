# Generated by Django 4.1.1 on 2023-02-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_statia_poto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statia',
            name='poto',
            field=models.ImageField(default='defaul.png', upload_to='news_images', verbose_name='фото'),
        ),
    ]