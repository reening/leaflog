# Generated by Django 4.2.5 on 2023-09-10 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_alter_location_geom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taxon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rank', models.CharField(choices=[('class', 'Class'), ('subclass', 'Subclass'), ('order', 'Order'), ('suborder', 'Suborder'), ('family', 'Family'), ('subfamily', 'Subfamily'), ('tribe', 'Tribe'), ('subtribe', 'Subtribe'), ('genus', 'Genus'), ('subgenus', 'Subgenus'), ('section', 'Section'), ('subsection', 'Subsection'), ('series', 'Series'), ('subseries', 'Subseries'), ('species', 'Species'), ('subspecies', 'Subspecies'), ('variety', 'Variety'), ('subvariety', 'Subvariety'), ('cultivar', 'Cultivar'), ('form', 'Form'), ('subform', 'Subform')], max_length=20)),
                ('hybrid', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.taxon')),
            ],
            options={
                'verbose_name': 'taxon',
                'verbose_name_plural': 'taxa',
            },
        ),
    ]
