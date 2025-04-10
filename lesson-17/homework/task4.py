import pandas as pd
titanic = pd.read_csv('titanic.csv')
def filter_survivors(df):
    return df[df['Survived'] == 1]

def fill_age(df):
    return df.assign(Age=df['Age'].fillna(df['Age'].mean()))

def add_fare_per_age(df):
    return df.assign(Fare_Per_Age=df['Fare'] / df['Age'])

pipeline_titanic = (
    titanic
    .pipe(filter_survivors)
    .pipe(fill_age)
    .pipe(add_fare_per_age)
)
def filter_delayed_flights(df):
    return df[df['DepDelay'] > 30]

def add_delay_per_hour(df):
    return df.assign(Delay_Per_Hour=df['DepDelay'] / df['AirTime'])

pipeline_flights = (
    flights
    .pipe(filter_delayed_flights)
    .pipe(add_delay_per_hour)
)
