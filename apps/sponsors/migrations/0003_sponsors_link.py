# Generated by Django 2.2 on 2020-10-09 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0002_auto_20201001_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsors',
            name='link',
            field=models.URLField(blank=True, help_text="an external link to the sponsor's website.", null=True, verbose_name='link'),
        ),
    ]