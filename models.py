# models.py
from datetime import datetime
from config import db, ma
from sqlalchemy import Column, Integer, String

class Widget(db.Model):
    __tablename__ = "widgets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    number_of_parts = db.Column(db.Integer)
    created_date = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    updated_date = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

def __init__(self, **kwargs):
    super(Widget, self).__init__(**kwargs)

class WidgetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Widget
        load_instance = True
        sqla_session = db.session

widget_schema = WidgetSchema()
widgets_schema = WidgetSchema(many=True)
