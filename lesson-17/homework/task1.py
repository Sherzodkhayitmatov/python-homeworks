import pandas as pd
import sqlite3

conn = sqlite3.connect('chinnok.db')

customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)

joined = pd.merge(customers, invoices, on='CustomerId', how='inner')

invoice_count = joined.groupby(['CustomerId', 'FirstName', 'LastName']).InvoiceId.count().reset_index(name='Total_Invoices')



movies = pd.read_csv('movie.csv')

df1 = movies[['director_name', 'color']]
df2 = movies[['director_name', 'num_critic_for_reviews']]

left_join = pd.merge(df1, df2, on='director_name', how='left')
left_join_count = len(left_join)

full_outer_join = pd.merge(df1, df2, on='director_name', how='outer')
full_outer_join_count = len(full_outer_join)
