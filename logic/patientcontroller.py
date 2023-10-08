from flask import Blueprint, request, jsonify, render_template
from model_db import db, Appointment

bp = Blueprint('main', __name__)

@bp.route('/agendamiento', methods=['POST'])
def create_appointment():
    data = request.json
    new_appointment = Appointment(name=data['name'], date=data['date'], time=data['time'])
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment created successfully'}), 201

@bp.route('/agendamiento/<int:id>', methods=['PUT'])
def edit_appointment(id):
    appointment = Appointment.query.get(id)
    data = request.json
    appointment.name = data['name']
    appointment.date = data['date']
    appointment.time = data['time']
    db.session.commit()
    return jsonify({'message': 'Appointment updated successfully'}), 200

@bp.route('/agendamiento/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    appointment = Appointment.query.get(id)
    db.session.delete(appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment deleted successfully'}), 200


@bp.route('/agendamiento')
def appointment_form():
    return render_template('agendamiento.html')