# Generated by Django 4.0.6 on 2022-07-29 00:40

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('titulo_post', models.CharField(max_length=255, verbose_name='Título')),
                ('conteudo_post', models.TextField(verbose_name='Conteúdo')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('sobre', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
