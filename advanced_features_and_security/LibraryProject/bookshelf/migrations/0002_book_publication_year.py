# Generated by Django 5.1.2 on 2024-11-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
