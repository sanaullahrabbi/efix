# Generated by Django 3.2.13 on 2022-08-01 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20220721_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='equip_charge',
            field=models.FloatField(blank=True, default=0, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='tech_charge',
            field=models.FloatField(default=0, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customerrs', to='core.customuserregistration'),
        ),
    ]
