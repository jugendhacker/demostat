# Generated by Django 2.1.7 on 2019-02-27 13:48

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('demostatapp', '0002_auto_20190225_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lat', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('lon', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='demo',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='link',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='organisation',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='demo',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='demostatapp.Location'),
        ),
        migrations.AlterField(
            model_name='demo',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='demostatapp.Organisation'),
        ),
        migrations.AlterField(
            model_name='demo',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='link',
            name='demo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='demostatapp.Demo'),
        ),
    ]
