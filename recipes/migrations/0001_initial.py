# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Recipe'
        db.create_table('recipes_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('recipes', ['Recipe'])


    def backwards(self, orm):
        
        # Deleting model 'Recipe'
        db.delete_table('recipes_recipe')


    models = {
        'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['recipes']
