from app import app, db
from flask import jsonify, request, render_template
from app.models import Trip
from datetime import datetime


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@app.route('/trip', methods=['GET'])
def get_trip():
    return jsonify([u.to_dict() for u in Trip.query.all()])

@app.route('/trip/<int:trip_id>', methods=['GET'])
def get_trips(trip_id):
    return jsonify(Trip.query.get(trip_id).to_dict())

@app.route('/start/<string:starttime>', methods=['GET'])
def get_time(starttime):
    starttimed = datetime.strptime(starttime, "%m/%d/%y %H:%M")
    return jsonify(Trip.query.get(starttimed).to_dict())


@app.route('/end/<string:stoptime>', methods=['GET'])
def get_end(stoptime):
    stoptimed = datetime.strptime(stoptime, "%m/%d/%y %H:%M")
    return jsonify(Trip.query.get(stoptimed).to_dict())

@app.route('/bike', methods=['GET'])
def get_bike():
    return jsonify([b.to_dict() for b in Trip.query.all()])

@app.route('/bike/<int:bikeid>', methods=['GET'])
def get_bikes(bikeid):
    return jsonify(Trip.query.get(bikeid).to_dict())
