# Generated by Django 3.1 on 2020-08-28 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0047_auto_20200810_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostalCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(unique=True, verbose_name='code')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_time', models.TimeField()),
                ('delivery_zones', models.ManyToManyField(to='delivery.PostalCode')),
                ('from_address', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='from_address', to='account.address')),
                ('to_address', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='to_address', to='account.address')),
            ],
        ),
    ]
