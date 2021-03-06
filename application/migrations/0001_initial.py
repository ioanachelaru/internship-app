# Generated by Django 3.1.5 on 2021-01-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('cv', models.FileField(blank=True, default=None, null=True, upload_to='./cvs')),
            ],
        ),
    ]
