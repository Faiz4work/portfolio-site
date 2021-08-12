from flask import Blueprint, render_template, request, redirect, url_for
from portfolio_site import mail
from flask_mail import Message


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
    return render_template('sections/portfolio.html')


@main.route('/email', methods=["POST"])
def email():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')
    print(name)
    print(email)
    print(subject)
    print(message)
    form_msg = Message(subject + f" ({email})", sender=email, 
                            recipients=['faizahmed11234@gmail.com', 'admin@faiz4work.com'], 
                            body=message)
    mail.send(form_msg)
    print("Email sent!")
    return redirect(url_for('main.home'))