# Generated by Django 5.1.2 on 2024-10-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Learning_App', '0002_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='photo',
            field=models.CharField(default='img/user/inconnu.jpg', max_length=50, null=True),
        ),
    ]