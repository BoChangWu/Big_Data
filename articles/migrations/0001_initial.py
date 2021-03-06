# Generated by Django 4.0.3 on 2022-03-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('img_url', models.CharField(max_length=200)),
                ('article_id', models.CharField(max_length=50)),
                ('article_order', models.IntegerField()),
                ('related_art', models.CharField(max_length=200)),
            ],
        ),
    ]
