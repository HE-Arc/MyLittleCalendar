# Generated by Django 2.0.2 on 2018-02-25 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20180225_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fk_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Address'),
        ),
    ]
