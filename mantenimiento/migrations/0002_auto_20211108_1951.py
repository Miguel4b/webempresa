# Generated by Django 3.2.8 on 2021-11-08 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lugar',
            options={'verbose_name': 'Lugar', 'verbose_name_plural': 'Lugares'},
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=10, verbose_name='area')),
                ('Descripcion', models.CharField(max_length=100, verbose_name='descripcion')),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.lugar')),
            ],
            options={
                'verbose_name': 'área',
                'verbose_name_plural': 'áreas',
            },
        ),
    ]