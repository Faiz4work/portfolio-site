from flask import Flask, render_template
from flask_mail import Mail, Message
from portfolio_site.config import Config

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)

    from portfolio_site.main.routes import main
    app.register_blueprint(main)

    return app