# Generated by Django 4.0.4 on 2022-05-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('book', 'Book'), ('PostersPrints', 'Posters & Prints'), ('RIDINGBOOTS&CHAPS ', 'RIDINGBOOTS&CHAPS '), ('ChildrensRidingWear', 'Childrens Riding Wear'), ('Helmets', 'Helmets'), ('Gloves', 'Gloves'), ('WomensTights&Breeches', 'WomensTights&Breeches'), ('BodyProtectors', 'Body Protectors'), ('WomensRidingClothing', 'Womens Riding Clothing')], max_length=200, null=True),
        ),
    ]
