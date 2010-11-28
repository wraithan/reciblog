from django.db import models
from django.template.defaultfilters import slugify

import tagging


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)


class Entry(models.Model):
    class Status:
        LIVE = 1
        PENDING = 2
        CHOICES = (
            (LIVE, 'Live'),
            (PENDING, 'Pending'),
            )
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True)
    author = models.ForeignKey('auth.user')
    content = models.TextField()
    status = models.IntegerField(choices=Status.CHOICES,
                                 default=Status.PENDING)
    allow_comments = models.BooleanField(default=True)
    publish = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    recipes = models.ManyToManyField('recipes.Recipe', related_name='entries', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='entries', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Entries'
        ordering = ('-publish',)


    def save(self):
        self.slug = slugify(self.name)
        super(Entry, self).save()


tagging.register(Entry)
