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
    return jsonify(widgets[int(id)])

@app.post("/widgets")
def add_widget():
    print("c")
    params = {
        'name': request.values.get('name'),
        'number_of_parts': request.values.get('number_of_parts'),
        'created_at': request.values.get('created_at'),
        'updated_at': request.values.get('updated_at')
    }
    new_widget = Widget(params)
    # new_widget.input()
    # new_widget = Widget()
    # new_widget = widget_schema.load(widget, session=db.session)
    print(new_widget)
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
