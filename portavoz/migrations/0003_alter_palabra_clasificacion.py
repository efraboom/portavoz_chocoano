# Generated by Django 3.2 on 2022-02-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portavoz', '0002_alter_palabra_clasificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palabra',
            name='clasificacion',
            field=models.CharField(choices=[('afro', 'Afro'), ('embera', 'Embera')], default='afro', max_length=16),
        ),
    ]
