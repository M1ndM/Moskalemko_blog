# Generated by Django 3.0.3 on 2020-02-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('key_word', models.CharField(max_length=100)),
            ],
        ),
    ]
