# Generated by Django 5.1.1 on 2024-10-11 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartamento', '0001_initial'),
        ('morador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='morador',
            name='numero_casa',
        ),
        migrations.AddField(
            model_name='morador',
            name='apartamento',
            field=models.ForeignKey(default=11111111111, on_delete=django.db.models.deletion.PROTECT, to='apartamento.apartamento', verbose_name='Apartamento'),
            preserve_default=False,
        ),
    ]
