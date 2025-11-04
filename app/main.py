from flask import Flask
from .config import Config
from .routes import bp
from .tasks import init_scheduler, scheduled_job, scheduler


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(bp)

    # scheduler job ekleme
    if app.config.get("APSCHEDULER_ENABLED"):
        try:
            scheduler.add_job(
                id="heartbeat",
                func=scheduled_job,
                trigger="interval",
                seconds=300
            )
            init_scheduler(app)
        except Exception:
            app.logger.exception("Scheduler başlatılırken hata")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
