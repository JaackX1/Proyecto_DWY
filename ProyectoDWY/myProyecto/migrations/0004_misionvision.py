# Generated by Django 2.2.16 on 2020-10-22 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProyecto', '0003_insumos'),
    ]

    operations = [
        migrations.CreateModel(
            name='MisionVision',
            fields=[
                ('ident', models.CharField(max_length=115, primary_key=True, serialize=False)),
                ('mision', models.TextField()),
                ('vision', models.TextField()),
            ],
        ),
    ]
