# Generated by Django 4.2.6 on 2024-03-14 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('culture', '0005_rename_dateend_showcaseorder_date_end_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtifactTransportAct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_transport', models.DateTimeField(verbose_name='Дата передачи экспонато')),
                ('artifacts', models.ManyToManyField(to='culture.artifact', verbose_name='Передаваемые артифакты на выставку')),
                ('showcase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.showcaseorder', verbose_name='Приказ о проведении выставки')),
            ],
            options={
                'verbose_name': 'Акт передачи экспонатов на выставку',
                'verbose_name_plural': 'Акты передачи экспонатов на выставки',
            },
        ),
    ]
