# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///./Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Routes
#################################################

# /api/v1.0/precipitation
# /api/v1.0/stations
# /api/v1.0/tobs



@app.route("/api/v1.0/precipitation")
# def send():
#     if request.method == "POST":
#         nickname = request.form["nickname"]
#         age = request.form["age"]

#         pet = Pet(nickname=nickname, age=age)
#         db.session.add(pet)
#         db.session.commit()

#         return "Thanks for the form data!"

#     return render_template("form.html")


@app.route("/api/v1.0/stations")
# def list_pets():
#     results = db.session.query(Pet.nickname, Pet.age).all()

#     pets = []
#     for result in results:
#         pets.append({
#             "nickname": result[0],
#             "age": result[1]
#         })
#     return jsonify(pets)


@app.route("/api/v1.0/tobs)
# def home():
#     return "Welcome!"


if __name__ == "__main__":
    app.run()
