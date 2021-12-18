from flask import Blueprint
from flask.templating import render_template

quote = Blueprint("quote", __name__)

@quote.route('/quote')
def quote_page():
    return render_template("quote/quote_form.html")