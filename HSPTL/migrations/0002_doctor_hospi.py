# Generated by Django 4.0.5 on 2022-08-02 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HSPTL', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='hospi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HSPTL.hospital'),
        ),
    ]
