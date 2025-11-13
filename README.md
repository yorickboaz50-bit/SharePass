# SharePass

Een minimale Flask-applicatie die een healthcheck endpoint aanbiedt zodat clients geen 404 foutmelding meer krijgen op de hoofdpagina.

## Ontwikkeling

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
flask --app app run
```

## Testen

```bash
pytest
```
