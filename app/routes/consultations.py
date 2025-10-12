from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from ..extensions import db
from ..models.consultation import Consultation
from ..models.patient import Patient
from ..models.professional import Professional
from datetime import datetime

bp = Blueprint('consultations', __name__)

@bp.get('/')
@jwt_required()
def listar():
    cons = Consultation.query.all()
    return [
        {
            'id': c.id,
            'patient_id': c.patient_id,
            'professional_id': c.professional_id,
            'scheduled_at': c.scheduled_at.isoformat(),
            'notes': c.notes
        } for c in cons
    ]

@bp.post('/')
@jwt_required()
def criar():
    data = request.get_json() or {}
    patient_id = data.get('patient_id')
    professional_id = data.get('professional_id')
    scheduled_at = data.get('scheduled_at')
    notes = data.get('notes')

    if not patient_id or not professional_id or not scheduled_at:
        return {'msg': 'patient_id, professional_id e scheduled_at são obrigatórios'}, 400

    if not Patient.query.get(patient_id):
        return {'msg': 'patient_id inválido'}, 400
    if not Professional.query.get(professional_id):
        return {'msg': 'professional_id inválido'}, 400

    try:
        dt = datetime.fromisoformat(scheduled_at)
    except Exception:
        return {'msg': 'scheduled_at deve estar em ISO 8601'}, 400

    c = Consultation(patient_id=patient_id, professional_id=professional_id, scheduled_at=dt, notes=notes)
    db.session.add(c)
    db.session.commit()
    return {'id': c.id}, 201

@bp.get('/<int:cid>')
@jwt_required()
def obter(cid):
    c = Consultation.query.get_or_404(cid)
    return {
        'id': c.id,
        'patient_id': c.patient_id,
        'professional_id': c.professional_id,
        'scheduled_at': c.scheduled_at.isoformat(),
        'notes': c.notes
    }

@bp.put('/<int:cid>')
@jwt_required()
def atualizar(cid):
    c = Consultation.query.get_or_404(cid)
    data = request.get_json() or {}
    if 'patient_id' in data:
        c.patient_id = data['patient_id']
    if 'professional_id' in data:
        c.professional_id = data['professional_id']
    if 'scheduled_at' in data:
        try:
            from datetime import datetime as _dt
            c.scheduled_at = _dt.fromisoformat(data['scheduled_at'])
        except Exception:
            return {'msg': 'scheduled_at inválido (ISO 8601)'}, 400
    if 'notes' in data:
        c.notes = data['notes']
    db.session.commit()
    return {'msg': 'updated'}

@bp.delete('/<int:cid>')
@jwt_required()
def excluir(cid):
    c = Consultation.query.get_or_404(cid)
    db.session.delete(c)
    db.session.commit()
    return {'msg': 'deleted'}
