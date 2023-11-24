import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('ds_salaries.csv')[['experience_level', 'employment_type', 'job_title', 'salary_in_usd', 'remote_ratio', 'company_size']]
print(df.columns)