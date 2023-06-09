# Generated by Django 4.1.7 on 2023-02-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('quantity_type', models.CharField(blank=True, choices=[('KG', 'KG'), ('Gram', 'Gram'), ('Ton', 'Ton'), ('Piece', 'Piece')], max_length=60, null=True)),
                ('category', models.CharField(blank=True, choices=[('Fruits', 'Fruits'), ('Vagetable', 'Vagetable'), ('Oil', 'Oil'), ('Rice', 'Rice'), ('Others', 'Others')], max_length=60, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
