from flask import Flask, render_template
from flask_mail import Mail
from portfolio_site.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

mail = Mail()
db = SQLAlchemy()
admin = Admin()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)
    db.init_app(app)
    admin.init_app(app)

    from portfolio_site.admin import myadmin
    app.register_blueprint(myadmin)

    from portfolio_site.main.routes import main
    app.register_blueprint(main)

    from portfolio_site.quote.routes import quote
    app.register_blueprint(quote)

    return app