# Documentação rápida da API

## Autenticação
- `POST /auth/signup` – cria usuário
- `POST /auth/login` – retorna `access_token`

## Pacientes (`Authorization: Bearer <token>`)
- `GET /patients/` – lista pacientes
- `POST /patients/` – cria paciente `{ "name": "...", "cpf": "..." }`
- `GET /patients/{id}` – detalhe
- `PUT /patients/{id}` – atualiza
- `DELETE /patients/{id}` – remove

## Profissionais
- CRUD semelhante a pacientes. `role` ∈ {`medico`,`enfermeiro`,`tecnico`}.

## Consultas
- `POST /consultations/`
```json
{"patient_id":1,"professional_id":1,"scheduled_at":"2025-10-20T10:30:00","notes":"Retorno"}
```
