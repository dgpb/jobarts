import django_filters
from django_filters import CharFilter

from .models import Job


class JobFilter(django_filters.FilterSet):
    job_title = CharFilter(lookup_expr='icontains', label='')

    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['company', 'company_url', 'description', 'salary', 'district', 'publication_date', 'job_url', 'job_title', 'city']
