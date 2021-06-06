# Generated by Django 3.0.5 on 2021-05-24 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=20)),
                ('link_img', models.CharField(max_length=50)),
                ('Ram', models.CharField(max_length=10)),
                ('Bonhotrong', models.CharField(max_length=50)),
                ('Pin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Noi_ban',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100)),
                ('link_img', models.CharField(blank=True, max_length=100, null=True)),
                ('price_sale', models.IntegerField()),
                ('price_goc', models.IntegerField(blank=True, null=True)),
                ('brand', models.CharField(blank=True, max_length=20, null=True)),
                ('manhinh', models.CharField(blank=True, max_length=50, null=True)),
                ('hedieuhanh', models.CharField(blank=True, max_length=50, null=True)),
                ('cameratruoc', models.CharField(blank=True, max_length=20, null=True)),
                ('CPU', models.CharField(blank=True, max_length=50, null=True)),
                ('Ram', models.CharField(blank=True, max_length=10, null=True)),
                ('Bonhotrong', models.CharField(blank=True, max_length=50, null=True)),
                ('Pin', models.CharField(blank=True, max_length=50, null=True)),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='backend.Key')),
                ('noi_ban', models.ForeignKey(db_column='id_noiban', on_delete=django.db.models.deletion.CASCADE, to='backend.Noi_ban')),
            ],
        ),
    ]