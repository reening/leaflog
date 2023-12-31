# Generated by Django 4.2.5 on 2023-10-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0008_alter_accession_collected'),
    ]

    operations = [
        migrations.AddField(
            model_name='accession',
            name='material',
            field=models.CharField(choices=[('p', 'Whole plant'), ('s', 'Seed or spore'), ('v', 'Vegetative part (cutting)'), ('t', 'Tissue culture'), ('o', 'Other')], default='o', max_length=1),
        ),
    ]
