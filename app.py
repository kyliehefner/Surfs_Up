# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Create a database engine
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Make references for tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session link between Python and SQLite Database
session = Session(engine)

# Create a new Flask instance
app = Flask(__name__)

# Create welcome root for Flask routes
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br>
    Available Routes:<br>
    /api/v1.0/precipitation<br>
    /api/v1.0/stations<br>
    /api/v1.0/tobs<br>
    /api/v1.0/temp/start/end
    ''')

# Create precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate date one year from last date in data set
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Perform a query to retrieve the precipitation scores
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    # Create dictionary with date as key and precipitation as value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Create stations route
@app.route("/api/v1.0/stations")
def stations():
    # Query all stations in database
    results = session.query(Station.station).all()
    # Unravel results into array and then convert to list
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Create monthly temp route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    # Calculate date one year from last date in data set
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query the last year of temperature observation data from primary station
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    # Unravel results into array and then convert to list
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Create statistics route
@app.route("/api/v1.0/temp/<start>")

@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    # List with min, avg, and max temps
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        # Query db based on min, avg, max list
        # Asterisk indicates multiple results from query
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        # Unravel results into array and then convert to list
        temps = list(np.ravel(results))
        return jsonify(temps)

    # Find min, avg, and max temps between start and end date
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    # Unravel results into array and then convert to list
    temps = list(np.ravel(results))
    return jsonify(temps)