"""Script simples para popular dados de exemplo."""
from datetime import datetime, timedelta
from app import create_app
from app.extensions import db
from app.models import User, Role, Patient, Professional, ProfessionalRole, Consultation

app = create_app()
with app.app_context():
    db.create_all()

    if not User.query.filter_by(email='admin@sghss.com').first():
        admin = User(email='admin@sghss.com', role=Role.ADMIN)
        admin.set_password('Senha123')
        db.session.add(admin)

    # pacientes
    p1 = Patient(name='João Silva'); p1.set_cpf('123.456.789-00')
    p2 = Patient(name='Maria Oliveira'); p2.set_cpf('987.654.321-00')
    db.session.add_all([p1, p2])

    # profissionais
    d1 = Professional(name='Dra. Ana Paula', role=ProfessionalRole.MEDICO, license='CRM 12345')
    n1 = Professional(name='Enf. Carlos', role=ProfessionalRole.ENFERMEIRO, license='COREN 67890')
    db.session.add_all([d1, n1])
    db.session.commit()

    # consultas
    c1 = Consultation(patient_id=p1.id, professional_id=d1.id, scheduled_at=datetime.utcnow()+timedelta(days=1), notes='Primeira avaliação')
    db.session.add(c1)
    db.session.commit()
    print('Seeds inseridos.')
