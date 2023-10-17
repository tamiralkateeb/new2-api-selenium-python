from datetime import datetime
from config import db, ma

# Define db model to allow working with SQLAlchemy
class Person(db.Model):
    __tablename__ = "person"  # You need to use '__tablename__' instead of '__table_name__'
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(100), index=True)
    fname = db.Column(db.String(100))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

# Marshmallow Schema
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # Set SQLAlchemy model into model
        model = Person
        # Set SQLAlchemy db session into Marshmallow
        sqla_session = db.session
        load_instance = True  # Use True instead of true
