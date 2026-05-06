"""Skill Analyzer"""
from collections import Counter
class SkillAnalyzer:
    def analyze_skills(self, jobs):
        all_skills = []
        for job in jobs:
            all_skills.extend(job.get('skills', []))
        return {'top_skills': list(set(all_skills))}
