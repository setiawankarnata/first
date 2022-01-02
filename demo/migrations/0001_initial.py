# Generated by Django 4.0 on 2021-12-29 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, unique=True)),
                ('description', models.TextField(blank=True, max_length=256)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4)),
                ('published', models.DateField(blank=True, default=None, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('cover', models.FileField(upload_to='covers/')),
            ],
        ),
    ]
