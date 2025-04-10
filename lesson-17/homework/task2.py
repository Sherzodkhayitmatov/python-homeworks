from shutil import move
import pandas as pd

titanic = pd.read_csv('titanic.csv')

grouped = titanic.groupby('Pclass').agg({
    'Age': 'mean',
    'Fare': 'sum',
    'PassengerId': 'count'  # Assuming PassengerId is unique
}).rename(columns={'PassengerId': 'Passenger_Count'}).reset_index()

grouped_movies = move.groupby(['color', 'director_name']).agg({
    'num_critic_for_reviews': 'sum',
    'duration': 'mean'
}).reset_index()


flights = pd.read_csv('flights.csv')

grouped_flights = flights.groupby(['Year', 'Month']).agg({
    'FlightNum': 'count',
    'ArrDelay': 'mean',
    'DepDelay': 'max'
}).rename(columns={'FlightNum': 'Total_Flights'}).reset_index()
