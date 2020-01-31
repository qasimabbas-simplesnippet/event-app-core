# Generated by Django 3.0.2 on 2020-01-31 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelines', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['event', 'start_time', 'ordering'], 'verbose_name': 'section', 'verbose_name_plural': 'sections'},
        ),
        migrations.AddField(
            model_name='section',
            name='cover',
            field=models.ImageField(blank=True, help_text='an optional cover to show in section page.', null=True, upload_to='', verbose_name='cover'),
        ),
        migrations.AddField(
            model_name='section',
            name='ordering',
            field=models.SmallIntegerField(default=0, help_text="the object's position, in relation to it's siblings.", verbose_name='ordering'),
        ),
        migrations.AlterField(
            model_name='section',
            name='type',
            field=models.CharField(choices=[('generic', 'Generic'), ('talk', 'Talks'), ('performance', 'Performance'), ('activity', 'Activity'), ('entertainment', 'Entertainment')], help_text="shows type of this program section, whether it's a generic section, a talk or performance, an activity, or else.", max_length=31, verbose_name='type'),
        ),
    ]