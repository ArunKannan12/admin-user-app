# Generated by Django 3.2.20 on 2023-08-19 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='static/images/uploads')),
                ('app_category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('points', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_earned', models.PositiveIntegerField(default=0)),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='static/images/screenshots/')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.admin_task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
