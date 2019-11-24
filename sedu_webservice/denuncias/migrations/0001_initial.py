# Generated by Django 2.2.6 on 2019-11-24 16:06

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
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
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Setor',
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
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='TipoReclamacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.Setor')),
            ],
            options={
                'db_table': 'denuncias_tipo_reclamacao',
            },
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('sre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.SRE')),
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
                ('cod_linha', models.CharField(blank=True, default='', max_length=60)),
                ('protocolo', models.CharField(default='', max_length=60)),
                ('data_ocorrido', models.DateTimeField()),
                ('agencia_transporte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='denuncias.AgenciaTransporte')),
                ('aluno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='denuncias.Aluno')),
                ('reclamante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='denuncias.Reclamante')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='denuncias.ReclamacaoStatus')),
                ('tipo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='denuncias.TipoReclamacao')),
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
                ('cod_ibge', models.CharField(max_length=200)),
                ('sre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.SRE')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
                ('cod_inep', models.CharField(max_length=200)),
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
                ('reclamacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='denuncias.Reclamacao')),
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
    ]
