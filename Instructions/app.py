# import necessary libraries

import pandas as pd
import datetime as data
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

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
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Routes
#################################################

# /api/v1.0/precipitation
# /api/v1.0/stations
# /api/v1.0/tobs

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii temperature and precipitation API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
    )



@app.route("/api/v1.0/precipitation")

def precipitation():
    """Return the precipitation data as json"""

    return jsonify(precipitation)



@app.route("/api/v1.0/stations")

def stations():
    """Return the station data as json"""

    return jsonify(stations)




@app.route("/api/v1.0/tobs)

def tobs():
    """Return the tobs data as json"""

    return jsonify(tobs)


if __name__ == "__main__":
    app.run()
