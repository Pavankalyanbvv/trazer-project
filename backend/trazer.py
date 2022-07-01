from distutils.log import debug
import sqlite3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def db_conn():
    conn = None
    try:
        conn = sqlite3.connect('tdb.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn


class display(Resource):
    def get(self):
        conn = db_conn()
        cursor = conn.cursor()
        cursor = conn.execute("select * from vehicles order by Id desc limit 7")
        count = [dict(date=r[1], pedestain=r[2],LMV=r[7], total_count=r[12]) for r in cursor.fetchall()]
        return count

class datecnt(Resource):
    def get(self, dte):
        conn = db_conn()
        cursor = conn.cursor()
        cursor = conn.execute("select * from vehicles ")
        count = [dict(date=r[1], pedestain=r[2],LMV=r[7],total_count=r[4]) for r in cursor.fetchall() if r[1]==dte]
        return count

api.add_resource(display, '/vc')
api.add_resource(datecnt, '/vc/<string:dte>')


if __name__ == '__main__':
    app.run(debug=True)
