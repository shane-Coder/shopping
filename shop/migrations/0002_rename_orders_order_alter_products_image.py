# Generated by Django 4.2.2 on 2023-08-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='orders',
            new_name='Order',
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='picture/items/'),
        ),
    ]
