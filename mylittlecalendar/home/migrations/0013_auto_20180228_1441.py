# Generated by Django 2.0.2 on 2018-02-28 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20180228_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fk_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Address'),
        ),
    ]