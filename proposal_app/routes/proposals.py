# Proposal management routes
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required
from database.db import db
from database.models import Proposal, Client

proposals_bp = Blueprint('proposals', __name__)

@proposals_bp.route('/proposals')
@login_required
def list_proposals():
    proposals = Proposal.query.order_by(Proposal.created_at.desc()).all()
    clients = Client.query.all()
    return render_template('dashboard/proposals.html', proposals=proposals, clients=clients)

@proposals_bp.route('/proposals/create', methods=['GET', 'POST'])
@login_required
def create_proposal():
    if request.method == 'POST':
        client_id = request.form.get('client_id')
        title = request.form.get('title')
        description = request.form.get('description')
        amount = request.form.get('amount', 0.0)
        
        if not client_id or not title:
            flash('Cliente y título son obligatorios', 'error')
            return redirect(url_for('proposals.list_proposals'))
        
        proposal = Proposal(
            client_id=client_id,
            title=title,
            description=description,
            amount=float(amount) if amount else 0.0,
            status='draft'
        )
        
        db.session.add(proposal)
        db.session.commit()
        
        flash('Propuesta creada exitosamente', 'success')
        return redirect(url_for('proposals.list_proposals'))
    
    clients = Client.query.all()
    return render_template('dashboard/proposals.html', clients=clients)

@proposals_bp.route('/proposals/<int:id>/edit', methods=['POST'])
@login_required
def edit_proposal(id):
    proposal = Proposal.query.get_or_404(id)
    
    proposal.client_id = request.form.get('client_id', proposal.client_id)
    proposal.title = request.form.get('title', proposal.title)
    proposal.description = request.form.get('description', proposal.description)
    proposal.amount = float(request.form.get('amount', proposal.amount))
    proposal.status = request.form.get('status', proposal.status)
    
    db.session.commit()
    
    flash('Propuesta actualizada exitosamente', 'success')
    return redirect(url_for('proposals.list_proposals'))

@proposals_bp.route('/proposals/<int:id>/delete', methods=['POST'])
@login_required
def delete_proposal(id):
    proposal = Proposal.query.get_or_404(id)
    db.session.delete(proposal)
    db.session.commit()
    
    flash('Propuesta eliminada exitosamente', 'success')
    return redirect(url_for('proposals.list_proposals'))

@proposals_bp.route('/proposals/<int:id>/preview')
@login_required
def preview_proposal(id):
    proposal = Proposal.query.get_or_404(id)
    return render_template('dashboard/preview.html', proposal=proposal)

@proposals_bp.route('/proposals/<int:id>')
@login_required
def get_proposal(id):
    proposal = Proposal.query.get_or_404(id)
    return jsonify({
        'id': proposal.id,
        'client_id': proposal.client_id,
        'title': proposal.title,
        'description': proposal.description,
        'amount': proposal.amount,
        'status': proposal.status
    })

