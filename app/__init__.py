"""SharePass application package."""

from flask import Flask, jsonify


def create_app() -> Flask:
    """Application factory."""

    app = Flask(__name__)

    @app.get("/")
    def healthcheck() -> tuple[str, int]:
        """Healthcheck endpoint to confirm the service is reachable."""

        payload = {"status": "ok", "message": "SharePass API is running"}
        return jsonify(payload), 200

    return app


app = create_app()
