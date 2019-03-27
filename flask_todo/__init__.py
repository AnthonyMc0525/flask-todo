from flask import Flask, request, make_response, render_template

import psycopg2

from . import db




def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
                                
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


    @app.route('/', methods=['GET', 'POST', 'PUT'])
    def index():
        rows = db.show_todos() 
        
        return render_template('index.html', items=rows)


    @app.route("/create", methods=['GET', 'POST'])
    # This page is for creating new todos
    def create_todo():
        return render_template('create_todo.html')

    @app.route("/update", methods=['GET', 'PUT'])
    # This page is for update new todos
    def update_todo():
        return render_template('update_todo.html')
    
    return app

