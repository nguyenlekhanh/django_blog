# Generated by Django 4.1 on 2023-11-16 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_category_slug_alter_contact_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(default='b6dedbcb-e649-4cbd-94ef-4d4db0392833', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]
