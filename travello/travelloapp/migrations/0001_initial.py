# Generated by Django 4.1.7 on 2023-03-23 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='traveller_det',
            fields=[
                ('tr_name', models.CharField(max_length=128)),
                ('tr_age', models.IntegerField()),
                ('tr_gender', models.CharField(max_length=6)),
                ('tr_phnum', models.IntegerField()),
                ('tr_aadar', models.IntegerField(primary_key=True, serialize=False)),
                ('tr_image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
