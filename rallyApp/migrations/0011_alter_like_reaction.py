# Generated by Django 3.2.15 on 2022-10-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rallyApp', '0010_auto_20221006_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='reaction',
            field=models.BooleanField(choices=[(0, 'Like'), (1, 'Unlike')], default=0),
        ),
    ]
