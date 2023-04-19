import psycopg2
from psycopg2.extras import DictCursor
import os

# "postgres://localhost:5432"
connection = psycopg2.connect(os.getenv("POSTGRES_URI"))

cursor = connection.cursor(cursor_factory=DictCursor)

cursor.execute("SELECT * FROM posts")
rows = cursor.fetchall()

print(rows[0]["title"])

cursor.close()
connection.close()
