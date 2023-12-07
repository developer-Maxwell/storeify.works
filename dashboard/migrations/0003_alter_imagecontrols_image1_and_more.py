# Generated by Django 4.2.4 on 2023-12-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0002_imagecontrols_alter_emailmarketing_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagecontrols",
            name="image1",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="dashboard"
            ),
        ),
        migrations.AlterField(
            model_name="imagecontrols",
            name="image2",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="dashboard"
            ),
        ),
        migrations.AlterField(
            model_name="imagecontrols",
            name="image3",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="dashboard"
            ),
        ),
        migrations.AlterField(
            model_name="imagecontrols",
            name="image4",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="dashboard"
            ),
        ),
        migrations.AlterField(
            model_name="imagecontrols",
            name="image5",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="dashboard"
            ),
        ),
        migrations.AlterField(
            model_name="imagecontrols",
            name="image6",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="dashboard"
            ),
        ),
    ]
