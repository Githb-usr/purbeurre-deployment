# Generated by Django 3.2.3 on 2021-06-27 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='Mot de passe')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Dernière connexion')),
                ('is_superuser', models.BooleanField(default=False, help_text='Indique que cet utilisateur a toutes les permissions sans les attribuer explicitement.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Indique si l\'utilisateur peut se connecter à ce site d\'administration.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Création du compte')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Pseudonyme')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Prénom')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nom')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Adresse email')),
                ('avatar', models.ImageField(upload_to='')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière modification')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='Les groupes auxquels appartient cet utilisateur. Un utilisateur obtiendra toutes les permissions accordées à chacun de ses groupes.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='Groupes')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Autorisations spécifiques pour cet utilisateur.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='Permissions utilisateur')),
            ],
            options={
                'ordering': ('-created_at', '-updated_at'),
            },
        ),
        migrations.CreateModel(
            name='Substitute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('initial_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initial_product', to='food.product')),
                ('substituted_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='substituted_product', to='food.product')),
                ('users', models.ManyToManyField(related_name='substitutes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'substitutes',
            },
        ),
    ]