# Generated by Django 2.1.4 on 2018-12-15 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocsLinux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('ptit', models.CharField(max_length=255)),
                ('pptit', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('hits', models.IntegerField(default=0)),
            ],
        ),
    ]
