from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Location(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    geom = models.JSONField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('location-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Taxon(models.Model):
    class Meta:
        verbose_name = 'taxon'
        verbose_name_plural = 'taxa'

    TAXON_RANKS = [
        ('class', 'Class'),
        ('subclass', 'Subclass'),
        ('order', 'Order'),
        ('suborder', 'Suborder'),
        ('family', 'Family'),
        ('subfamily', 'Subfamily'),
        ('tribe', 'Tribe'),
        ('subtribe', 'Subtribe'),
        ('genus', 'Genus'),
        ('subgenus', 'Subgenus'),
        ('section', 'Section'),
        ('subsection', 'Subsection'),
        ('series', 'Series'),
        ('subseries', 'Subseries'),
        ('species', 'Species'),
        ('subspecies', 'Subspecies'),
        ('variety', 'Variety'),
        ('subvariety', 'Subvariety'),
        ('cultivar', 'Cultivar'),
        ('form', 'Form'),
        ('subform', 'Subform'),
    ]

    name = models.CharField(max_length=200)
    rank = models.CharField(max_length=20, choices=TAXON_RANKS)
    parent = models.ForeignKey('Taxon', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    hybrid = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return self.name
