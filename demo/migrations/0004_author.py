# Generated by Django 4.0 on 2022-01-03 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_character'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('books', models.ManyToManyField(related_name='book2author', to='demo.Book')),
            ],
        ),
    ]
