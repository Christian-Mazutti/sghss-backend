from datetime import datetime
from ..extensions import db

def cpf_somente_digitos(cpf: str) -> str:
    return ''.join(filter(str.isdigit, cpf or ''))

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)  # armazenado como dígitos
    birth_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_cpf(self, cpf_raw: str):
        self.cpf = cpf_somente_digitos(cpf_raw)

    def __repr__(self):
        return f'<Patient {self.name}>'
