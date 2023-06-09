# Generated by Django 4.1.4 on 2022-12-26 06:22

from django.db import migrations, models
import home.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='admin')),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='admin', validators=[home.validators.file_size]),
        ),
    ]
