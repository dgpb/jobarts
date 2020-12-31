from django.core.management.base import BaseCommand
from django.utils import timezone
from jobs.models import Job
import json
from datetime import datetime, date
import dateparser


class Command(BaseCommand):
    help = 'Set up the database'

    def handle(self, *args: str, **options: str):
        with open('static/jobs28122020Test.json', 'r') as handle:
            big_json = json.loads(handle.read())
            for item in big_json:
                if len(item['description']) == 0:
                    print('Not created. Description empty')
                    continue

                if item['publication_date'] != None:
                    dt = dateparser.parse(item['publication_date'])
                else:
                    dt = datetime.now()

                new_date = date(dt.year, dt.month, dt.day)

                existing_job = Job.objects.filter(

                    job_title = item['job_title'],
                    company = item['company'],
                    company_url = item['company_url'],
                    description = item['description'],
                    publication_date = new_date,
                    salary = item['salary'],
                    city = item['city'],
                    district = item['district'],
                    job_url = item['job_url'],
                    job_type = item['job_type'],

                )
                if existing_job.exists():
                    print('This Job already exist')
                else:
                    Job.objects.create(

                        job_title = item['job_title'],
                        company = item['company'],
                        company_url = item['company_url'],
                        description = item['description'],
                        publication_date = new_date,
                        salary = item['salary'],
                        city = item['city'],
                        district = item['district'],
                        job_url = item['job_url'],
                        job_type = item['job_type'],

                )

                self.stdout.write(self.style.SUCCESS('added jobs!'))
