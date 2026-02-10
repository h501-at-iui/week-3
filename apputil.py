import seaborn as sns
import pandas as pd


# Excercise 1
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Exercise 2
def to_binary(n):
    if n < 2:              # base case (stopping point)
        return str(n)
    else:
        return to_binary(n // 2) + str(n % 2)


# Ecercise 3
import pandas as pd

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

def task_1():
    # fix messy gender column
    df_bellevue['gender'] = df_bellevue['gender'].str.strip().str.lower()
    print("Cleaned gender column (removed spaces and standardized text).")

    # count missing values and sort
    missing_counts = df_bellevue.isna().sum().sort_values()

    # return sorted column names
    return list(missing_counts.index)

def task_2():
    admissions_per_year = df_bellevue.groupby('year').size().reset_index(name='total_admissions')
    return admissions_per_year

def task_3():
    # clean gender column just in case
    df_bellevue['gender'] = df_bellevue['gender'].str.strip().str.lower()

    avg_age = df_bellevue.groupby('gender')['age'].mean()
    return avg_age

def task_4():
    common_jobs = df_bellevue['profession'].value_counts().head(5)
    return list(common_jobs.index)

