# Generated by Django 3.1.7 on 2021-03-24 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insect_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, upload_to='')),
                ('placeholder', models.CharField(default=None, max_length=100)),
                ('insect', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='insects.insect')),
            ],
        ),
        migrations.CreateModel(
            name='Rect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('image', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='insects.insect_image')),
            ],
        ),
    ]
