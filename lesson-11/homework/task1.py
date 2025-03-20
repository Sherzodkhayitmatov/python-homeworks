import sqlite3

connection = sqlite3.connect('roster.db')
cursor = connection.cursor()


create_table = """
    CREATE TABLE Roster(
        Name TEXT,
        Species TEXT,
        Age INT
    );"""
cursor.execute(create_table) 

insert_table = """
    INSERT INTO Roster VALUES(
        'Benjamin Sisko',
        'Human',
        40
    )
  """
cursor.execute(insert_table)

data = [
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29),
]

cursor.executemany("INSERT INTO Roster VALUES (?,?,?)", data)

connection.commit()
connection.close()