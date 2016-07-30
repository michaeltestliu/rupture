# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-29 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breach', '0018_target_samplesize'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='batch',
            field=models.IntegerField(default=0, help_text='Which batch of the round is currently being attempted. A new batch starts any time samplesets for the round are created, either because the round is starting or because not enough condidence was built.'),
        ),
        migrations.AddField(
            model_name='sampleset',
            name='batch',
            field=models.IntegerField(default=0, help_text='The round batch that this sampleset belongs to.'),
        ),
        migrations.AddField(
            model_name='sampleset',
            name='records',
            field=models.IntegerField(default=0, help_text='The number of records that contain all the data.'),
        ),
        migrations.AddField(
            model_name='target',
            name='confidence_threshold',
            field=models.FloatField(default=1.0, help_text='The threshold that is used for confidence, in order to determine whether a candidate should be chosen.'),
        ),
        migrations.AddField(
            model_name='victim',
            name='calibration_wait',
            field=models.FloatField(default=0.0, help_text='The amount of time in seconds that sniffer should wait so that Scapy has enough time to lock on low-level network resources.'),
        ),
        migrations.AddField(
            model_name='victim',
            name='recordscardinality',
            field=models.IntegerField(default=0, help_text='The amount of expected TLS response records per request. If 0 then the amount is not known or is expected to change per request.'),
        ),
    ]