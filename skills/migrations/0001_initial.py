# Generated by Django 3.1.1 on 2020-09-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='portfolio/images')),
                ('name', models.CharField(max_length=200)),
                ('refer_link', models.URLField(blank=True)),
            ],
        ),
    ]
