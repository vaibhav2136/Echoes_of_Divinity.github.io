# Generated by Django 4.2.4 on 2023-08-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', upload_to='img'),
        ),
    ]
