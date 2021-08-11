from flask import Flask, render_template




def create_app():
    app = Flask(__name__)

    from portfolio_site.main.routes import main
    app.register_blueprint(main)

    return app