# -*- coding: utf-8 -*-
from django.db import models

# Notice that we are importing the gis models here
from django.contrib.gis.db import models

from autoslug import AutoSlugField
from django_extensions.db import fields as ext_fields

class Location(models.Model):
    name = models.CharField(max_length=255)

    # Automatically create slug based on the name field
    slug = AutoSlugField(populate_from='name', max_length=255)
    
    # Automatically create a unique id for this object
    uuid = ext_fields.UUIDField(auto=True)
    
    # Geo Django field to store a point
    point = models.PointField(help_text="Represented as (longitude, latitude)")

    # You MUST use GeoManager to make Geo Queries
    objects = models.GeoManager()

class Region(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', max_length=255)
    uuid = ext_fields.UUIDField(auto=True)
    #geometria = models.PolygonField(srid=4326, null=True, geography=True)
    # Geo Django field to store a polygon
    area = models.PolygonField()

    # You MUST use GeoManager to make Geo Queries
    objects = models.GeoManager()

# Create your models here.
