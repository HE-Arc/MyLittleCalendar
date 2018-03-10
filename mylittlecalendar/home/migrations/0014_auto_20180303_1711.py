# Generated by Django 2.0.2 on 2018-03-03 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20180228_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fk_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Address'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='images/events/default.jpg', upload_to='images/events'),
        ),
    ]