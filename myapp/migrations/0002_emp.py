# Generated by Django 3.0.5 on 2021-05-15 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('hiredate', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('commission', models.DecimalField(decimal_places=2, max_digits=6)),
                ('deptname', models.CharField(max_length=30)),
            ],
        ),
    ]
