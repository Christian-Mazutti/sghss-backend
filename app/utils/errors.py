from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({'erro': 'Requisição inválida'}), 400

    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify({'erro': 'Não autorizado'}), 401

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'erro': 'Recurso não encontrado'}), 404

    @app.errorhandler(500)
    def server_error(e):
        app.logger.exception('Erro interno do servidor')
        return jsonify({'erro': 'Erro interno do servidor'}), 500
