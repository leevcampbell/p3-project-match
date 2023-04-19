import sqlite3

CONN = sqlite3.connect("db/users.db")
CURSOR = CONN.cursor()