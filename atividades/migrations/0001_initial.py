# Generated by Django 4.0.3 on 2022-04-13 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cate_por_tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_autor', models.CharField(max_length=100)),
                ('conteudo_blog', models.TextField(max_length=10000)),
                ('titulo', models.CharField(max_length=100)),
                ('imagem', models.ImageField(blank=True, upload_to='')),
                ('publicado', models.DateTimeField(auto_now_add=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='atividades.cate_por_tipo')),
            ],
        ),
    ]
