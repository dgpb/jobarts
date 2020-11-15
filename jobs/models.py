from django.db import models

# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    company_url = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    salary = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    district = models.CharField(max_length=200, null=True, blank=True)
    publication_date = models.DateTimeField(default=None)
    job_url = models.CharField(max_length=200, null=True, blank=True)
    job_type = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.job_title
