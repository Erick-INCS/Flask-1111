#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Our flask routes """

from app import app
from flask import jsonify, g
import sqlite3

DATABASE = 'mypage'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/aboutme")
def aboutme():
    return jsonify(
        first_name='Erick', 
        last_name="Arroyo", 
        hobby="Play piano"
    )

@app.route('/users')
def get_users():
    cursor = get_db().execute('SELECT * FROM user', ())
    result = cursor.fetchall()
    cursor.close()
    #return jsonify(result)

    result = {'ok': True,
            'body': list(map(lambda u: 
                {
                    'first_name': u[0], 
                    'last_name': u[1], 
                    'hobby': u[2]
                }, result))
            }

    return result;
