# Generated by Django 4.0.3 on 2022-03-18 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ichki',
            name='bolim',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bolim_ichkilari', to='asosiy.bolim'),
        ),
    ]
