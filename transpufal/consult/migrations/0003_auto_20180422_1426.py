# Generated by Django 2.0.4 on 2018-04-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0002_auto_20180422_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='archive',
            field=models.FileField(help_text='Um arquivo .pdf com todos os documentos do processo', upload_to='uploads/'),
        ),
    ]
