# Generated by Django 2.2.6 on 2019-11-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_delete_publicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id_publicacion', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('nombre_prof', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=350)),
            ],
        ),
    ]
