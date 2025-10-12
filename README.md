# SGHSS – Sistema de Gestão Hospitalar e de Serviços de Saúde (Back-end)

Projeto acadêmico com ênfase **Back-end** em **Python + Flask**. O objetivo é demonstrar
um serviço simples de cadastro de **Pacientes**, **Profissionais** e **Consultas**, com
**autenticação JWT**, **migrações** e **testes via Postman**.

> Observação: é um protótipo didático. Telemedicina/vídeo não foram implementados.

## Como executar (passo a passo)
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
cp .env.exemplo .env

# cria/migra o banco local (SQLite)
flask --app app db init
flask --app app db migrate -m "tabelas iniciais"
flask --app app db upgrade

# (opcional) popular alguns dados
python scripts/seeds.py

# subir a API
flask --app app run --debug
```

- URL base: `http://127.0.0.1:5000`
- Documentação rápida de rotas: `docs/API.md`
- Coleção Postman: `tests/SGHSS.postman_collection.json`

## Variáveis de ambiente (.env)
```
FLASK_ENV=development
SECRET_KEY=troque_esta_chave
JWT_SECRET_KEY=troque_este_jwt
DATABASE_URL=sqlite:///sghss.db
LOG_FILE=logs/app.log
```

## Estrutura
```
app/
  models/        # modelos do banco
  routes/        # blueprints (auth, patients, professionals, consultations)
  utils/         # helpers (decorators, tratamento de erro)
  services/      # (futuro) regras de negócio
docs/
prints/          # screenshots para o relatório
scripts/         # seeds e utilitários
tests/           # coleção Postman
```

## Licença
Uso educacional.
