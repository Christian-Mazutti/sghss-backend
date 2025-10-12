from datetime import datetime
from ..extensions import db

class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey('professional.id'), nullable=False)
    scheduled_at = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    patient = db.relationship('Patient', lazy='joined')
    professional = db.relationship('Professional', lazy='joined')

    def __repr__(self):
        return f'<Consultation {self.id} {self.scheduled_at.isoformat()}>'
