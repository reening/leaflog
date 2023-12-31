from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.text import slugify
from django.utils.timezone import now


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
    display_name = models.CharField(max_length=200)
    rank = models.CharField(max_length=20, choices=TAXON_RANKS)
    parent = models.ForeignKey('Taxon', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    hybrid = models.BooleanField(blank=False, null=False, default=False)

    def get_absolute_url(self):
        return reverse('taxon-detail', kwargs={'pk': self.id})
    
    def __str__(self):
        return self.name

    def _get_parent_rank(self, rank):
        parent = self.parent
        while parent:
            if parent.rank == rank:
                return parent.name

            parent = parent.parent

        return ''

    def _get_parent_genus(self):
        return self._get_parent_rank('genus')

    def _get_parent_species(self):
        return self._get_parent_rank('species')

    def get_name_display(self):
        if self.rank == 'genus':
            return f'<i>{self.name}</i>'
        elif self.rank == 'subgenus':
            genus = self._get_parent_genus()
            return f'<i>{genus}</i> subg. <i>{self.name}</i>'
        elif self.rank == 'species':
            genus = self._get_parent_genus()
            return f'<i>{genus}</i> <i>{self.name}</i>'
        elif self.rank == 'subspecies':
            genus = self._get_parent_genus()
            species = self._get_parent_species()
            return f'<i>{genus}</i> <i>{species}</i> subsp. <i>{self.name}</i>'
        elif self.rank == 'variety':
            genus = self._get_parent_genus()
            species = self._get_parent_species()
            return f'<i>{genus}</i> <i>{species}</i> var. <i>{self.name}</i>'
        elif self.rank == 'subvariety':
            genus = self._get_parent_genus()
            species = self._get_parent_species()
            return f'<i>{genus}</i> <i>{species}</i> subvar. <i>{self.name}</i>'
        elif self.rank == 'cultivar':
            genus = self._get_parent_genus()
            species = self._get_parent_species()
            return f'<i>{genus}</i> <i>{species}</i> \'{self.name}\''
        elif self.rank == 'form':
            genus = self._get_parent_genus()
            species = self._get_parent_species()
            return f'<i>{genus}</i> <i>{species}</i> f. <i>{self.name}</i>'
            
        return self.name

    def get_rank_index(self):
        for i, rank in enumerate(self.TAXON_RANKS):
            if rank[0] == self.rank:
                return i

        return -1

    def save(self, *args, **kwargs):
        self.display_name = strip_tags(self.get_name_display())
        super().save(*args, **kwargs)

    def to_json(self):
        data = {
            'id': self.id,
            'name': self.name,
            'displayName': strip_tags(self.get_name_display()),
            'displayNameHtml': self.get_name_display(),
            'rank': self.rank,
            'rankName': self.get_rank_display(),
            'rankOrder': self.get_rank_index(),
        }

        return data


class Accession(models.Model):
    ACCESSION_STATUS = [
        ('c', 'Current'),
        ('d', 'Non-current due to death'),
        ('t', 'Non-current due to transfer'),
        ('s', 'Stored in dormant state'),
        ('o', 'Other'),
    ]

    ACCESSION_MATERIAL = [
        ('p', 'Whole plant'),
        ('s', 'Seed or spore'),
        ('v', 'Vegetative part (cutting)'),
        ('t', 'Tissue culture'),
        ('o', 'Other'),
    ]

    accnum = models.CharField(max_length=200, verbose_name='Accession number', unique=True)
    taxon = models.ForeignKey('Taxon', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=1, choices=ACCESSION_STATUS, default='o')
    material = models.CharField(max_length=1, choices=ACCESSION_MATERIAL, default='o')
    source = models.CharField(max_length=200, null=True, blank=True)
    collected = models.DateField(default=now)
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('accession-detail', kwargs={'pk': self.id})
