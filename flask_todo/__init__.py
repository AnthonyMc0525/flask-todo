from flask import Flask, request, make_response, render_template

import psycopg2
from datetime import datetime





def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DB_NAME='flasktodo',
        DB_USER='flasktodo_user',
                                
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    
    from . import db
    db.init_app(app)


    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')


    @app.route("/create", methods=['GET', 'POST'])
    # This page is for creating new todos
    def create_todo():
        if request.method == 'GET':
            return render_template('create.html')

        elif request.method == 'POST':
            new_item = request.form['task']
            conn = get_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO todo_items(name, completed, date_added) VALUES (%s, %s, %s)", (new_item, False, datetime.now()))


            return render_template('create.html')
    return app
