"""Graduate Job Market Intelligence Platform"""
import pandas as pd
from scrapers.job_scraper import JobScraper
from models.salary_predictor import SalaryPredictor
from analytics.skill_analyzer import SkillAnalyzer

class JobMarketPlatform:
    def __init__(self):
        self.scraper = JobScraper()
        self.salary_predictor = SalaryPredictor()
        self.skill_analyzer = SkillAnalyzer()
    
    def analyze_market(self, job_title, location):
        """Analyze job market for given role"""
        jobs = self.scraper.scrape_jobs(job_title, location, limit=100)
        
        # Analyze salaries
        salary_insights = self.salary_predictor.analyze_salaries(jobs)
        
        # Analyze skills
        skill_insights = self.skill_analyzer.analyze_skills(jobs)
        
        return {
            'jobs_found': len(jobs),
            'salary_insights': salary_insights,
            'skill_insights': skill_insights
        }

def main():
    print("Job Market Intelligence Platform")
    platform = JobMarketPlatform()
    results = platform.analyze_market("Data Engineer", "San Francisco")
    print(f"\nJobs Found: {results['jobs_found']}")
    print(f"Avg Salary: ${results['salary_insights']['avg_salary']:,.0f}")
    print(f"Top Skills: {', '.join(results['skill_insights']['top_skills'][:5])}")

if __name__ == "__main__":
    main()
