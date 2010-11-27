# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.template.defaultfilters import slugify
from blog.models import Entry

class Migration(DataMigration):

    def forwards(self, orm):
        entries = Entry.objects.all()
        for e in entries:
            e.slug = slugify(e.name)
            e.save()


    def backwards(self, orm):
        "Write your backwards methods here."


    models = {
        'blog.entry': {
            'Meta': {'object_name': 'Entry'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'recipes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'entries'", 'symmetrical': 'False', 'to': "orm['recipes.Recipe']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['blog']
