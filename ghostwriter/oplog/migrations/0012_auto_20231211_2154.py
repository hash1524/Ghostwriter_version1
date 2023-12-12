# Generated by Django 3.2.19 on 2023-12-11 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oplog', '0011_auto_20230323_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='oplogentry',
            name='entry_identifier',
            field=models.CharField(blank=True, help_text='Integrations may use this to track log entries.', max_length=65535, null=True, verbose_name='Identifier'),
        ),
        migrations.AddIndex(
            model_name='oplogentry',
            index=models.Index(fields=['oplog_id', 'entry_identifier'], name='oplog_oplog_oplog_i_0e03f5_idx'),
        ),
    ]
