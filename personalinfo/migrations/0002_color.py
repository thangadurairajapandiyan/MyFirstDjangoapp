# Generated by Django 2.2.5 on 2021-04-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clr', models.CharField(max_length=100)),
            ],
        ),
    ]
