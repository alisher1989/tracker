# Generated by Django 2.2 on 2019-09-25 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, verbose_name='status')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='type')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=50, verbose_name='summary')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='descripton')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task_status', to='webapp.Task', verbose_name='status')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task_type', to='webapp.Task', verbose_name='type')),
            ],
        ),
    ]