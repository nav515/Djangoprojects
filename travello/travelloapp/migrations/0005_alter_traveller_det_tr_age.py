# Generated by Django 4.1.7 on 2023-03-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelloapp', '0004_alter_traveller_det_tr_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveller_det',
            name='tr_age',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]