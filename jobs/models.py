from django.db import models

# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    company_url = models.URLField(max_length=200)
    description = models.TextField()
    salary = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    publication_date = models.CharField(max_length=200)
    job_url = models.CharField(max_length=200)
    job_type = models.CharField(max_length=200)

    def __str__(self):
        return self.job_title
