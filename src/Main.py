import sqlite3

connection = sqlite3.connect('FamousQuotes.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS FamousQuotes (Person TEXT PRIMARY KEY, Quotes TEXT)''')
cursor.execute("INSERT INTO FamousQuotes (Person, Quotes) VALUES ('A Cinderlla Story', 'Never let the fear of striking out keep you from playing the game.')")

connection.commit()
connection.close()

