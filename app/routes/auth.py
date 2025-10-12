from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token
from ..extensions import db
from ..models.user import User, Role

bp = Blueprint('auth', __name__)

@bp.post('/signup')
def signup():
    """Cria um usuário simples para acessar a API."""
    data = request.get_json() or {}
    email = data.get('email', '').strip().lower()
    password = data.get('password')
    role = data.get('role', 'user')

    if not email or not password:
        return {'msg': 'email e password são obrigatórios'}, 400

    if User.query.filter_by(email=email).first():
        return {'msg': 'email já registrado'}, 409

    try:
        role_enum = Role(role)
    except Exception:
        role_enum = Role.USER

    user = User(email=email, role=role_enum)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    current_app.logger.info('Usuário criado: %s', email)
    return {'id': user.id, 'email': user.email, 'role': user.role.value}, 201

@bp.post('/login')
def login():
    """Autentica e retorna um token JWT de acesso."""
    data = request.get_json() or {}
    email = data.get('email', '').strip().lower()
    password = data.get('password')
    if not email or not password:
        return {'msg': 'credenciais inválidas'}, 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return {'msg': 'credenciais inválidas'}, 401

    access_token = create_access_token(identity=user.id, additional_claims={'role': user.role.value})
    current_app.logger.info('Login efetuado: %s', email)
    return jsonify(access_token=access_token)
