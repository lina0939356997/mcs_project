from flask import Flask
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from apps.broker import bp as broker_bp
from apps.kanban import bp as kanban_bp
from apps.declare import bp as declare_bp
from apps.mock_pos import bp as mock_bp
from apps.mc import bp as mc_bp
from exts import db, mail, scheduler
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(mc_bp)
    app.register_blueprint(mock_bp)
    app.register_blueprint(declare_bp)
    app.register_blueprint(kanban_bp)
    app.register_blueprint(broker_bp)
    db.app = app
    db.init_app(app)
    mail.init_app(app)
    CSRFProtect(app)
    scheduler.init_app(app)
    scheduler.start()
    migrate = Migrate(app, db)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
