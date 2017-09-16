#!/usr/bin/env python

from flask import Flask, render_template, request
from script.robdd import ROBDD
import json

app = Flask(__name__,static_url_path="/static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/test", methods = ['POST'])
def greet():
    raw_cubes = []

    if request.form['cubes'] is not None:
        raw_cubes = request.form['cubes'].split(',')
    else:
        return ''
    stlen = len(raw_cubes[0])
    for cube in raw_cubes:
        if len(cube) != stlen:
            return 'Please provide valid cubes'

    robdd = ROBDD(raw_cubes)
    robdd.traverse()
    return robdd.makeJSON()


@app.route("/api/demo",methods = ['POST'])
def fun():
    return "Your request has " + json.dumps(request.form)


if __name__ == '__main__':
    app.run()
