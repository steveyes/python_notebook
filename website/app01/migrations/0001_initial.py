# Generated by Django 3.1.6 on 2021-05-11 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('content', models.CharField(max_length=255)),
                ('article_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.articletype')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.category')),
            ],
        ),
    ]
