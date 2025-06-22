import sqlite3

#define connection and cursor

connection = sqlite3.connect("data.sqlite")
cursor = connection.cursor()

command1 = '''
  CREATE TABLE vocab (
    id INTEGER PRIMARY KEY,
    vocab STRING
  )
'''

cursor.execute(command1)