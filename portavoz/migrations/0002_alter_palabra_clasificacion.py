# Generated by Django 3.2 on 2022-02-10 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portavoz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palabra',
            name='clasificacion',
            field=models.CharField(choices=[('afro', 'Afro'), ('embera', 'Embera')], default='choco', max_length=16),
        ),
    ]
