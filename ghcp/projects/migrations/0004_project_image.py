# Generated by Django 5.0.2 on 2024-02-25 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_demo'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default=0, upload_to='projects'),
            preserve_default=False,
        ),
    ]
