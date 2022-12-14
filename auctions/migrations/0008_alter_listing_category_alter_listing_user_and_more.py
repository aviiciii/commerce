# Generated by Django 4.1 on 2022-10-03 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('books', 'Books'), ('bussiness', 'Business & Industrial'), ('clothing', 'Clothing, Shoes & Accessories'), ('collectibles', 'Collectibles'), ('electronics', 'Consumer Electronics'), ('crafts', 'Crafts'), ('dolls', 'Dolls & Bears'), ('home', 'Home & Garden'), ('motor', 'Motors'), ('pets', 'Pet Supplies'), ('sports', 'Sporting Goods'), ('mobile', 'Mobile Phones/Gadgets'), ('merch', 'Merchandise, Cards & Fan Shop'), ('toys', 'Toys & Hobbies'), ('antiques', 'Antiques'), ('computers', 'Computers/Tablets & Networking'), ('others', 'Others')], max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bids_won', to=settings.AUTH_USER_MODEL),
        ),
    ]
