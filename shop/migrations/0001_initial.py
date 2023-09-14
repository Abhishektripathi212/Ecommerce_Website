# Generated by Django 4.2.5 on 2023-09-14 15:07

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
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('quantity', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tags',
                'indexes': [models.Index(fields=['id', 'deleted_at'], name='tags_id_790241_idx')],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=300)),
                ('Price', models.SmallIntegerField()),
                ('stock', models.SmallIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.category')),
                ('tags', models.ManyToManyField(blank=True, default=list, to='shop.tag')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['id', 'deleted_at'], name='categories_id_d9af82_idx'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.products'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cart_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='products',
            index=models.Index(fields=['id', 'deleted_at'], name='products_id_cf883d_idx'),
        ),
        migrations.AddIndex(
            model_name='cart',
            index=models.Index(fields=['id', 'deleted_at'], name='cart_id_61240c_idx'),
        ),
    ]