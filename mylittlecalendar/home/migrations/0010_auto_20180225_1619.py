# Generated by Django 2.0.2 on 2018-02-25 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20180225_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fk_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Address'),
        ),
    ]
