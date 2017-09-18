#!/usr/bin/env python

from flask import Flask, render_template, request
import script.robdd as robdd
import math
import json
import sys

app = Flask(__name__,static_url_path="/static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/test", methods = ['POST'])
def greet():

    if request.form['cubes'] is not None:
        raw_cubes = request.form['cubes'].split(',')
    else:
        return ''
    stlen = len(raw_cubes[0])
    for cube in raw_cubes:
        if len(cube) != stlen:
            return 'Please provide valid cubes'
    lim = max([len(word) for word in raw_cubes]) / 2
    size = int(math.pow(2, lim))
    array = robdd.makeArray(raw_cubes, size)
    newArr = robdd.traverse(array, size - 1)
    iteStr = robdd.ite(newArr[0])
    returnObj = '{"robdd":'+ robdd.makeJSON(newArr[0])+', "ite":"'+iteStr+'"}'
    return returnObj


@app.route("/api/demo",methods = ['POST'])
def fun():
    return "Your request has " + json.dumps(request.form)


if __name__ == '__main__':
    app.run()
