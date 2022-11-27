# Generated by Django 4.1.2 on 2022-11-02 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Size',
            field=models.CharField(default=2, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buyer',
            name='pic4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
    ]
