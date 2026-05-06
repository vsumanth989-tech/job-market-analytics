"""Job Scraper"""
import random
class JobScraper:
    def scrape_jobs(self, title, location, limit=100):
        jobs = []
        for i in range(min(limit, 100)):
            jobs.append({'title': title, 'salary': random.randint(80000, 150000), 'skills': ['Python', 'SQL', 'AWS']})
        return jobs
