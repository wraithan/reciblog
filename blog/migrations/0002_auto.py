# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    depends_on = (
        ('recipes', "0001_initial"),
    )

    def forwards(self, orm):
        
        # Adding M2M table for field recipes on 'Entry'
        db.create_table('blog_entry_recipes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entry', models.ForeignKey(orm['blog.entry'], null=False)),
            ('recipe', models.ForeignKey(orm['recipes.recipe'], null=False))
        ))
        db.create_unique('blog_entry_recipes', ['entry_id', 'recipe_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field recipes on 'Entry'
        db.delete_table('blog_entry_recipes')


    models = {
        'blog.entry': {
            'Meta': {'object_name': 'Entry'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'recipes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'entries'", 'symmetrical': 'False', 'to': "orm['recipes.Recipe']"}),
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
