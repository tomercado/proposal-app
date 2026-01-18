# Client management routes
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required
from database.db import db
from database.models import Client

clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/clients')
@login_required
def list_clients():
    clients = Client.query.order_by(Client.created_at.desc()).all()
    return render_template('dashboard/clients.html', clients=clients)

@clients_bp.route('/clients/add', methods=['POST'])
@login_required
def add_client():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    company = request.form.get('company')
    address = request.form.get('address')
    
    if not name:
        flash('El nombre del cliente es obligatorio', 'error')
        return redirect(url_for('clients.list_clients'))
    
    client = Client(
        name=name,
        email=email,
        phone=phone,
        company=company,
        address=address
    )
    
    db.session.add(client)
    db.session.commit()
    
    flash('Cliente agregado exitosamente', 'success')
    return redirect(url_for('clients.list_clients'))

@clients_bp.route('/clients/<int:id>/edit', methods=['POST'])
@login_required
def edit_client(id):
    client = Client.query.get_or_404(id)
    
    client.name = request.form.get('name', client.name)
    client.email = request.form.get('email', client.email)
    client.phone = request.form.get('phone', client.phone)
    client.company = request.form.get('company', client.company)
    client.address = request.form.get('address', client.address)
    
    db.session.commit()
    
    flash('Cliente actualizado exitosamente', 'success')
    return redirect(url_for('clients.list_clients'))

@clients_bp.route('/clients/<int:id>/delete', methods=['POST'])
@login_required
def delete_client(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    
    flash('Cliente eliminado exitosamente', 'success')
    return redirect(url_for('clients.list_clients'))

@clients_bp.route('/clients/<int:id>')
@login_required
def get_client(id):
    client = Client.query.get_or_404(id)
    return jsonify({
        'id': client.id,
        'name': client.name,
        'email': client.email,
        'phone': client.phone,
        'company': client.company,
        'address': client.address
    })

