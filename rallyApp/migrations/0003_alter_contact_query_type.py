# Generated by Django 3.2.15 on 2022-09-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rallyApp', '0002_alter_contact_query_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='query_type',
            field=models.CharField(choices=[(0, 'Question'), (1, 'Sponsorship'), (2, 'Other')], default=0, max_length=11),
        ),
    ]
