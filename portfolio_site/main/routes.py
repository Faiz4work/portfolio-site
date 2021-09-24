from flask import Blueprint, render_template, request, redirect, url_for
from portfolio_site import mail
from flask_mail import Message
from sqlalchemy import desc
from portfolio_site.models import *

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template("index.html")

@main.route('/web_development')
def web_development():
    return render_template("sections/services_page/web_development.html")

@main.route('/web_scraping')
def web_scraping():
    return render_template("sections/services_page/web_scraping.html")

@main.route('/ecommerce')
def ecommerce():
    return render_template("sections/services_page/ecommerce.html")

@main.route('/api')
def api():
    return render_template("sections/services_page/api.html")

@main.route('/portfolio')
def portfolio():
    portfolio_list = Portfolio.query.order_by(desc("id")).all()
    return render_template('sections/portfolio2.html', portfolio_list=portfolio_list)


@main.route('/email', methods=["POST"])
def email():
    name = request.json['name']
    email = request.json['email']
    subject = request.json['subject']
    message = request.json['message']
    form_msg = Message(subject + f" ({email})", sender=email, 
                            recipients=['faizahmed11234@gmail.com', 'admin@faiz4work.com'], 
                            body=message)

    try:
        mail.send(form_msg)
        print("Email sent!")
    except:
        print("Email is not sent due to some reasons")
    return "done"