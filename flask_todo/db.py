import psycopg2

import click
from flask import current_app, g
from flask.cli import with_appcontext

# connect using psycog2
connection = psycopg2.connect("dbname=todo_app host=localhost")

# Activate connection cursor
cur = connection.cursor()

# Select table and display
def show_todos():
    cur.execute('SELECT * FROM todo_items') 
    rows = cur.fetchall()

    return rows

# Insert data
# show table after you insert
def insert_into(name, date):
    cur.execute("INSERT INTO todo_items (name, completed, date_added) VALUES (%s, %s, %s)", (name, False, date))
    communication.commit()

    cur.execute('SELECT * FROM todo_items') 
    rows = cur.fetchall()

    return rows

