# Generated by Django 2.1.5 on 2019-02-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190212_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='isi',
            field=models.TextField(),
        ),
    ]