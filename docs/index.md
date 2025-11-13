---
layout: default
title: SharePass
---

# SharePass

SharePass is een minimale Flask-applicatie die een healthcheck-endpoint aanbiedt zodat clients geen 404-foutmelding meer ontvangen op de hoofdpagina. De applicatie start een webserver met Flask en exposeert een `/health` route die een JSON-respons teruggeeft met de status van de service.

## Gebruik

Start een lokale ontwikkelomgeving met:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
flask --app app run
```

Navigeer vervolgens naar `http://localhost:5000/health` om de healthcheck te bekijken.

## Testen

Voer de unit tests uit met:

```bash
pytest
```

Deze commando's corresponderen met de instructies in de README van dit project, zodat de GitHub Pages-documentatie synchroon loopt met de broncode.
