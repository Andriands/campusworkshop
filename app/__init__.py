"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpqvg64dad9donegthg-a.oregon-postgres.render.com",
        database="todo_demo_9r3p",
        user="todo_demo_9r3p_user",
        password="fdbfU5wwYqIufMMpIKpnOxD12ucvJE0i")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
