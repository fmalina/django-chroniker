# Generated by Django 3.0.6 on 2020-07-09 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chroniker', '0005_shorten_param_val'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Command group',
            },
        ),
        migrations.AddField(
            model_name='job',
            name='command_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chroniker.CommandGroup'),
        ),
        migrations.AddField(
            model_name='parameter',
            name='command_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chroniker.CommandGroup'),
        ),
    ]