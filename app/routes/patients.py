from flask import Blueprint, request, current_app
from flask_jwt_extended import jwt_required
from ..extensions import db
from ..models.patient import Patient

bp = Blueprint('patients', __name__)

@bp.get('/')
@jwt_required()
def listar():
    pacientes = Patient.query.all()
    return [{'id': p.id, 'name': p.name, 'cpf': p.cpf} for p in pacientes]

@bp.post('/')
@jwt_required()
def criar():
    data = request.get_json() or {}
    name = (data.get('name') or '').strip()
    cpf = (data.get('cpf') or '').strip()
    if not name or not cpf:
        return {'msg': 'name e cpf são obrigatórios'}, 400
    p = Patient(name=name)
    p.set_cpf(cpf)
    db.session.add(p)
    db.session.commit()
    current_app.logger.info('Paciente criado: %s', name)
    return {'id': p.id, 'name': p.name, 'cpf': p.cpf}, 201

@bp.get('/<int:pid>')
@jwt_required()
def obter(pid):
    p = Patient.query.get_or_404(pid)
    return {'id': p.id, 'name': p.name, 'cpf': p.cpf}

@bp.put('/<int:pid>')
@jwt_required()
def atualizar(pid):
    p = Patient.query.get_or_404(pid)
    data = request.get_json() or {}
    p.name = data.get('name', p.name) or p.name
    cpf = data.get('cpf')
    if cpf:
        p.set_cpf(cpf)
    db.session.commit()
    return {'id': p.id, 'name': p.name, 'cpf': p.cpf}

@bp.delete('/<int:pid>')
@jwt_required()
def excluir(pid):
    p = Patient.query.get_or_404(pid)
    db.session.delete(p)
    db.session.commit()
    current_app.logger.info('Paciente excluído: %s', p.id)
    return {'msg': 'deleted'}
