from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from ..extensions import db
from ..models.professional import Professional, ProfessionalRole

bp = Blueprint('professionals', __name__)

@bp.get('/')
@jwt_required()
def listar():
    pros = Professional.query.all()
    return [{'id': p.id, 'name': p.name, 'role': p.role.value, 'license': p.license} for p in pros]

@bp.post('/')
@jwt_required()
def criar():
    data = request.get_json() or {}
    name = (data.get('name') or '').strip()
    role = data.get('role')
    license = (data.get('license') or '').strip() or None
    if not name or not role:
        return {'msg': 'name e role são obrigatórios'}, 400
    try:
        role_enum = ProfessionalRole(role)
    except Exception:
        return {'msg': 'role inválido'}, 400
    p = Professional(name=name, role=role_enum, license=license)
    db.session.add(p)
    db.session.commit()
    return {'id': p.id, 'name': p.name, 'role': p.role.value, 'license': p.license}, 201

@bp.get('/<int:pid>')
@jwt_required()
def obter(pid):
    p = Professional.query.get_or_404(pid)
    return {'id': p.id, 'name': p.name, 'role': p.role.value, 'license': p.license}

@bp.put('/<int:pid>')
@jwt_required()
def atualizar(pid):
    p = Professional.query.get_or_404(pid)
    data = request.get_json() or {}
    p.name = data.get('name', p.name) or p.name
    role = data.get('role')
    if role:
        try:
            p.role = ProfessionalRole(role)
        except Exception:
            return {'msg': 'role inválido'}, 400
    p.license = data.get('license', p.license)
    db.session.commit()
    return {'id': p.id, 'name': p.name, 'role': p.role.value, 'license': p.license}

@bp.delete('/<int:pid>')
@jwt_required()
def excluir(pid):
    p = Professional.query.get_or_404(pid)
    db.session.delete(p)
    db.session.commit()
    return {'msg': 'deleted'}
