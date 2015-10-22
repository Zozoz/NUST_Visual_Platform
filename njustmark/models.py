#!/usr/bin/env python
# encoding: utf-8


from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='document/%Y/%m/%d')
