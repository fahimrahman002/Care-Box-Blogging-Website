# Generated by Django 4.1.7 on 2023-03-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0003_blog_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
