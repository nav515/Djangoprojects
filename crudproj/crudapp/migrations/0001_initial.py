# Generated by Django 4.1.7 on 2023-03-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpNum', models.IntegerField()),
                ('EmpName', models.CharField(max_length=64)),
                ('EmpSal', models.IntegerField()),
                ('EmpEmail', models.EmailField(max_length=64)),
                ('EmpDesc', models.TextField(max_length=100)),
            ],
        ),
    ]