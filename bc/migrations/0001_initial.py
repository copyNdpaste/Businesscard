# Generated by Django 2.1.7 on 2019-03-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Businesscard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=50)),
                ('company_addr', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('site_addr', models.CharField(max_length=50)),
            ],
        ),
    ]