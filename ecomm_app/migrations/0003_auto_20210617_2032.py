# Generated by Django 3.1.7 on 2021-06-17 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management_app', '0001_initial'),
        ('ecomm_app', '0002_auto_20210615_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_management_app.customer'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
