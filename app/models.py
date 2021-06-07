from app import db
from datetime import datetime as dt


class Trip(db.Model):
    trip_id = db.Column(db.Integer, primary_key=True)
    starttime = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    stoptime = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    bikeid = db.Column(db.Integer, nullable=False)
    from_station_id = db.Column(db.Integer, nullable=False)
    from_station_name = db.Column(db.String(125), nullable=False)
    to_station_id = db.Column(db.Integer, nullable=False)
    to_station_name = db.Column(db.String(125), nullable=False)
    usertype = db.Column(db.String(125), nullable=False)
    gender = db.Column(db.String(125))
    birthday = db.Column(db.String(125))
    trip_duration = db.Column(db.Integer)

    def to_dict(self):
        data = {
            'trip_id': self.trip_id,
            'starttime': self.starttime,
            'stoptime': self.stoptime,
            'bikeid': self.bikeid,
            'from_station_id': self.from_station_id,
            'from_station_name': self.from_station_name,
            'to_station_id': self.to_station_id,
            'to_station_name': self.to_station_name,
            'usertype': self.usertype,
            'gender': self.gender,
            'birthday': self.birthday,
            'trip_duration': self.trip_duration
        }
        return data
