from django.db import models


class SitesGroup(models.Model):
    title = models.CharField(
        max_length=256,
        help_text='A short descriptive title.',
    )
    sites = models.ManyToManyField(
        'sites.Site',
        help_text='Sites that belong to this group.',
    )
   
    def __unicode__(self):
        return self.title
