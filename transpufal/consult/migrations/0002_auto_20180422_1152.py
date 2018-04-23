# Generated by Django 2.0.4 on 2018-04-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='archive',
            field=models.FileField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='process',
            name='idcode',
            field=models.IntegerField(help_text='Número do processo'),
        ),
        migrations.AlterField(
            model_name='process',
            name='name',
            field=models.CharField(help_text='Nome do processo e do aluno', max_length=100),
        ),
    ]