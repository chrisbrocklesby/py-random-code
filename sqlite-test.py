import sqlite3
import os

connect = sqlite3.connect("db.sqlite")  # Path to database file
connect.row_factory = sqlite3.Row

sql = connect.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

sql.execute("""
      INSERT INTO movie VALUES
          ('Monty Python and the Holy Grail', 1975, 8.2),
          ('And Now for Something Completely Different', 1971, 7.5)
  """)

connect.commit()

rows = sql.execute("SELECT * FROM movie").fetchall()

print(rows[0]["title"])
