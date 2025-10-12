from datetime import datetime
from enum import Enum
from ..extensions import db

class ProfessionalRole(Enum):
    MEDICO = 'medico'
    ENFERMEIRO = 'enfermeiro'
    TECNICO = 'tecnico'

class Professional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.Enum(ProfessionalRole), nullable=False)
    license = db.Column(db.String(60), nullable=True)  # CRM/COREN/etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Professional {self.name} ({self.role.value})>'
