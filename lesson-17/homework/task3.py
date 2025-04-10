from shutil import move
import pandas as pd
titanic = pd.read_csv('titanic.csv')
def classify_age(age):
    return 'Child' if age < 18 else 'Adult'

titanic['Age_Group'] = titanic['Age'].apply(classify_age)
employee = pd.read_csv('employee.csv')

# Normalize within departments
employee['Normalized_Salary'] = employee.groupby('Department')['Salary'].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)
def classify_duration(duration):
    if duration < 60:
        return 'Short'
    elif duration <= 120:
        return 'Medium'
    else:
        return 'Long'

movies['Length_Category'] = movies['duration'].apply(classify_duration)
