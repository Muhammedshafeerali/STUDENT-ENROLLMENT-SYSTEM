# Generated by Django 3.2.14 on 2022-07-06 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('state', models.CharField(max_length=16, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('stdcode', models.AutoField(primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=16)),
                ('phoneNumber', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=16)),
                ('image', models.ImageField(upload_to='media/')),
                ('state', models.CharField(max_length=16)),
                ('district', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('district', models.CharField(max_length=16)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.state')),
            ],
        ),
    ]