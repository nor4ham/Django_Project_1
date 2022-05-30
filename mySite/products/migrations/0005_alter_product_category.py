# Generated by Django 4.0.4 on 2022-05-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_category_alter_product_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('book', 'Book'), ('PostersPrints', 'Posters & Prints')], max_length=200, null=True),
        ),
    ]
