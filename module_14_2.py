import sqlite3
import os

DB_NAME = 'not_telegram.db'

if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute(
        'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
        (f'User{i}', f'example{i}@gmail.com', i * 10, 1000)
    )

cursor.execute('''
UPDATE Users
SET balance = 500
WHERE id % 2 = 1
''')

cursor.execute('''
DELETE FROM Users
WHERE id % 3 = 1
''')

cursor.execute('''
DELETE FROM Users WHERE id = 6
''')

cursor.execute('''SELECT COUNT(*) FROM Users''')
total_users = cursor.fetchone()[0]

cursor.execute('''SELECT SUM(balance) FROM Users''')
all_balances = cursor.fetchone()[0]

average_balance = all_balances / total_users if total_users > 0 else 0
print(average_balance)

connection.commit()
connection.close()
