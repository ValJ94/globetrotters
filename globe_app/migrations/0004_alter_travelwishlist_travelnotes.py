# Generated by Django 3.2.5 on 2022-08-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globe_app', '0003_alter_travelwishlist_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelwishlist',
            name='travelNotes',
            field=models.TextField(blank=True),
        ),
    ]
