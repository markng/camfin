from django.db import models

class Candidate(models.Model):
    """Candidate for election"""
    name = models.CharField(max_length=255, null=True)
    def __unicode__(self):
        return(self.name)
    
class Document(models.Model):
    """Document with contributions"""
    candidate = models.ForeignKey("Candidate")
    title = models.CharField(max_length=255, null=True)

class Page(models.Model):
    """Page of document"""
    document = models.ForeignKey("Document")
    page_number = models.IntegerField()

class Position(models.Model):
    """Position within document"""
    page = models.ForeignKey("Page")
    position_number = models.IntegerField()

class Contribution(models.Model):
    """contribution to campaign fund"""
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    employer = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    candidate = models.ForeignKey("Candidate")
    position = models.ForeignKey("Position")
    user = models.ForeignKey("django.contrib.auth.models.User", null=True, blank=True)