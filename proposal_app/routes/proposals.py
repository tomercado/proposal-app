# Proposal management routes
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required
from database.db import db
from database.models import Proposal

proposals_bp = Blueprint('proposals', __name__)

@proposals_bp.route('/proposals')
@login_required
def list_proposals():
    proposals = Proposal.query.order_by(Proposal.created_at.desc()).all()
    return render_template('dashboard/proposals.html', proposals=proposals)

@proposals_bp.route('/proposals/create', methods=['GET', 'POST'])
@login_required
def create_proposal():
    if request.method == 'POST':
        client_name = request.form.get('client_name')
        title = request.form.get('title')
        intro_text = request.form.get('intro_text')
        content = request.form.get('content')
        
        if not client_name or not title:
            flash('Cliente y título son obligatorios', 'error')
            return redirect(url_for('proposals.list_proposals'))
        
        proposal = Proposal(
            client_name=client_name,
            title=title,
            intro_text=intro_text,
            content=content,
            status='draft'
        )
        
        db.session.add(proposal)
        db.session.commit()
        
        flash('Propuesta creada exitosamente', 'success')
        return redirect(url_for('proposals.list_proposals'))
    
    return render_template('dashboard/proposals.html')

@proposals_bp.route('/proposals/<int:id>/edit', methods=['POST'])
@login_required
def edit_proposal(id):
    proposal = Proposal.query.get_or_404(id)
    
    proposal.client_name = request.form.get('client_name', proposal.client_name)
    proposal.title = request.form.get('title', proposal.title)
    proposal.intro_text = request.form.get('intro_text', proposal.intro_text)
    proposal.content = request.form.get('content', proposal.content)
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
        'client_name': proposal.client_name,
        'title': proposal.title,
        'intro_text': proposal.intro_text,
        'content': proposal.content,
        'status': proposal.status
    })

