# Generated by Django 3.2.19 on 2023-05-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=1)),
                ('is_published', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
