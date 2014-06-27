# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Metric'
        db.create_table(u'crest_metric', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.TimeField')(auto_now=True, blank=True)),
            ('temp', self.gf('django.db.models.fields.FloatField')()),
            ('moist', self.gf('django.db.models.fields.FloatField')()),
            ('light', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'crest', ['Metric'])

        # Adding model 'Event'
        db.create_table(u'crest_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.TimeField')(auto_now=True, blank=True)),
            ('event', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crest', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Metric'
        db.delete_table(u'crest_metric')

        # Deleting model 'Event'
        db.delete_table(u'crest_event')


    models = {
        u'crest.event': {
            'Meta': {'object_name': 'Event'},
            'event': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'crest.metric': {
            'Meta': {'object_name': 'Metric'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'light': ('django.db.models.fields.FloatField', [], {}),
            'moist': ('django.db.models.fields.FloatField', [], {}),
            'temp': ('django.db.models.fields.FloatField', [], {}),
            'time': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['crest']