# Generated by Django 3.2 on 2022-02-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portavoz', '0004_auto_20220214_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palabra',
            name='clasificacion',
            field=models.CharField(choices=[('afro', 'Afro'), ('Embera Dóbida', 'Embera Dóbida')], default='afro', max_length=16),
        ),
    ]
