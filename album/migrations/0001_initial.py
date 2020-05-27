# Generated by Django 3.0.6 on 2020-05-27 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30)),
                ('image_description', models.CharField(max_length=30)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.ImageField(default='image url', upload_to='snaps/')),
                ('image_category', models.ManyToManyField(to='album.Category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.Location')),
            ],
            options={
                'ordering': ['date_posted'],
            },
        ),
    ]
