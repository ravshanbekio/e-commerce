# Generated by Django 4.0.3 on 2022-03-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtma', '0003_alter_buyurtma_savat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyurtma',
            name='savat',
            field=models.ManyToManyField(related_name='savatlar', related_query_name='savatlar', to='buyurtma.savat'),
        ),
    ]
