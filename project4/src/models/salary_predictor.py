"""Salary Predictor"""
import numpy as np
class SalaryPredictor:
    def analyze_salaries(self, jobs):
        salaries = [job['salary'] for job in jobs]
        return {'avg_salary': np.mean(salaries), 'median_salary': np.median(salaries)}
