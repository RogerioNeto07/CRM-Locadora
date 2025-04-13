# Generated by Django 5.1.2 on 2025-04-13 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_jogo_estoque'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('data', models.DateField(auto_now_add=True)),
                ('jogos', models.ManyToManyField(to='main.jogo')),
            ],
        ),
    ]
