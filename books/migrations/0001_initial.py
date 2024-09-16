# Generated by Django 5.0.6 on 2024-05-31 17:37

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
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='book_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('summary', models.TextField()),
            ],
        ),
    ]
