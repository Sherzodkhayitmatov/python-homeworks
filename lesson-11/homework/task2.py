import sqlite3

connection = sqlite3.connect('library.db')
cursor = connection.cursor()


create_table = """
    CREATE TABLE Library(
        Title: TEXT
        Author: TEXT
        Year_Published: INTEGER
        Genre: TEXT
    );"""
    
books =[
    ('To Kill a Mockingbird', 'Harper Lee', '1960', 'Fiction')
    ('1984', 'George Orwell', '1949', 'Dystopian')
    ('The Great Gatsby', 'F. Scott Fitzgerald', '1925', 'Classic')
]
cursor.executemany('INSERT INTO Books (Title, Author, Year_published, Genre) VALUES (?,?,?,?)', books)

# Update Year_Published of '1984' to 1950
cursor.execute("UPDATE Books SET Year_published = 1950 WHERE Title = '1984'")
# Retrieve and display Title and Author where Genre is 'Dystopian'
cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
dystopian_books = cursor.fetchall()
print("Dystopian books:")
for book in dystopian_books:
    print(book)
# Remove books published before 1950
cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
# Add new column Rating
cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
# Update Rating values
ratings = [
    (4.8, "To Kill a Mockingbird"),
    (4.7, "1984"),
    (4.5, "The Great Gatsby")
]
for rating, title in ratings:
    cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))

# Retrieve all books sorted by Year_Published in ascending order
cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
all_books = cursor.fetchall()
print("\nAll Books Sorted by Year Published:")
for book in all_books:
    print(book)

connection.commit()
connection.close()