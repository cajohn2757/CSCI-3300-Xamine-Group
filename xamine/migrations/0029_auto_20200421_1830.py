# Generated by Django 3.0.5 on 2020-04-21 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xamine', '0028_auto_20200419_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images',
                                    to='xamine.Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='completed',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='completed_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]