# Generated by Django 2.2.6 on 2019-11-07 18:38

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgenciaTransporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'denuncias_agencia_transporte',
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
                ('ra', models.CharField(default='', max_length=200)),
                ('cod_energia', models.CharField(default='', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReclamacaoStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'denuncias_reclamacao_status',
            },
        ),
        migrations.CreateModel(
            name='Reclamante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SRE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TipoReclamacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Superintendencia',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('sre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.SRE')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('superintendencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.Superintendencia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reclamacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('texto', models.TextField()),
                ('cod_linha', models.CharField(default='', max_length=60)),
                ('protocolo', models.CharField(default='', max_length=60)),
                ('agencia_transporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.AgenciaTransporte')),
                ('aluno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='denuncias.Aluno')),
                ('municipio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='denuncias.Municipio')),
                ('reclamante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='denuncias.Reclamante')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='denuncias.ReclamacaoStatus')),
                ('tipo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='denuncias.TipoReclamacao')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='municipio',
            name='superintendencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.Superintendencia'),
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.Municipio')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('texto', models.TextField()),
                ('reclamacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.Reclamacao')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.Responsavel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='aluno',
            name='escola',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.Escola'),
        ),
        migrations.AddField(
            model_name='agenciatransporte',
            name='sre',
            field=models.ManyToManyField(to='denuncias.SRE'),
        ),
        migrations.AddField(
            model_name='agenciatransporte',
            name='superintendencia',
            field=models.ManyToManyField(to='denuncias.Superintendencia'),
        ),
    ]
