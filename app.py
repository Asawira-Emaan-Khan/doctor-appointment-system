from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    speciality = db.Column(db.String(50), nullable=False)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.String(10), nullable=False)

with app.app_context():
    # Create the database tables
    db.create_all()

    # Populate the tables with initial data
    # Populate the tables with initial data
    for doctor_data in [
        {'firstName': "Muhammad Ali", 'lastName': "Kahoot", 'speciality': "DevOps"},
        {'firstName': "Good", 'lastName': "Doctor", 'speciality': "Test"}
    ]:
        doctor = Doctor(**doctor_data)
        db.session.add(doctor)

    db.session.commit()


    for appointment_data in [
        {'doctor_id': "1", 'date': "21 Nov 2023", 'rating': "Good"},
        {'doctor_id': "1", 'date': "22 Nov 2023", 'rating': "Bad"},
        {'doctor_id': "2", 'date': "22 Nov 2023", 'rating': "Good"},
        {'doctor_id': "1", 'date': "22 Nov 2023", 'rating': "Bad"},
        {'doctor_id': "2", 'date': "22 Nov 2023", 'rating': "Good"}
    ]:
        appointment = Appointment(**appointment_data)
        db.session.add(appointment)

    db.session.commit()


# Routes
@app.route('/')
def index():
    return "Hello, this is your Flask app!"

@app.route('/doctors')
def get_doctors():
    doctors = Doctor.query.all()
    doctor_list = [{'id': doctor.id, 'firstName': doctor.firstName, 'lastName': doctor.lastName, 'speciality': doctor.speciality} for doctor in doctors]
    return jsonify(doctor_list)

@app.route('/appointments')
def get_appointments():
    appointments = Appointment.query.all()
    appointment_list = [{'id': appointment.id, 'doctor_id': appointment.doctor_id, 'date': appointment.date, 'rating': appointment.rating} for appointment in appointments]
    return jsonify(appointment_list)

if __name__ == '__main__':
    app.run(debug=True)
