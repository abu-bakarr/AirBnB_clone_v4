#!/usr/bin/python3
""" Start Flask!!! """
from flask import Flask, render_template
from models import storage
from models import state


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(self):
    """ Removing SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def h1():
    """ Lists States """
    s = list(storage.all('State').values())
    s.sort(key=lambda state: state.name)
    return render_template('7-states_list.html', slist=s)


if __name__ == '__main__':
    app.run()
