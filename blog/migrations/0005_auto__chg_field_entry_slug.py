# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Entry.slug'
        db.alter_column('blog_entry', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=256, null=False))


    def backwards(self, orm):
        
        # Changing field 'Entry.slug'
        db.alter_column('blog_entry', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=256, null=True))


    models = {
        'blog.entry': {
            'Meta': {'object_name': 'Entry'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'recipes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'entries'", 'symmetrical': 'False', 'to': "orm['recipes.Recipe']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '256', 'db_index': 'True'}),
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
