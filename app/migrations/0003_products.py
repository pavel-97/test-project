# Generated by Django 2.1.1 on 2018-09-19 16:41

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180918_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('descriptions', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to=app.models.image_folder)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('available', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Categories')),
            ],
        ),
    ]
