from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import jsonify

def roles_required(*roles):
    """Decorator simples para restringir rotas por papel."""
    def wrapper(fn):
        @wraps(fn)
        def decorated(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get('role') not in roles:
                return jsonify({'msg': 'Acesso negado'}), 403
            return fn(*args, **kwargs)
        return decorated
    return wrapper
