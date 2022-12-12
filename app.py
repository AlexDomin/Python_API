# app.py
import sqlite3
import json
from flask import Flask, request, jsonify, make_response, abort, render_template
from config import db, app
from models import Widget, widget_schema, widgets_schema

def _find_next_id():
    return max(widget["id"] for widget in widgets) + 1

@app.get("/widgets")
def get_widgets():
    print("a")
    db.create_all()
    print(Widget)
    print(Widget.query)
    # print(Widget.query.get(1))
    # wd = Widget()
    widgets = Widget.query.all()
    for widget in widgets:
        print(dir(widget))
    return widgets_schema.dump(widgets)

@app.get("/widgets/<id>")
def get_widget(id):
    print("b")
    widget = db.session.get(Widget, id)
    if widget == None:
        return "not found", 404
    return widget_schema.dump(widget)

@app.post("/widgets")
def add_widget():
    print("c")
    new_widget = Widget()
    new_widget.name = request.json['name']
    new_widget.number_of_parts = request.json['number_of_parts']
    db.session.add(new_widget)
    db.session.commit()
    return widget_schema.dump(new_widget), 201

@app.put("/widgets/<id>")
def update_widget(id):
    print("d")
    widget = widgets[int(id)]
    name = request.json['name']
    number_of_parts = request.json['number of parts']
    widget["name"] = name
    widget["number of parts"] = number_of_parts
    
# @app.patch("/widgets/<id>")
# def edit_widget(id):
#     widget = widgets[int(id)]

@app.delete("/widgets/<id>")
def delete_widget(id):
    print("e")
    del widgets[int(id)]
    return {"success": "Requested widget has been successfully deleted!"}, 204
