from enum import unique
from portfolio_site import db
from datetime import datetime

class EmailLeads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String(70), unique=True, nullable=False)

    def __repr__(self):
        return f"Email: {self.email}, date_added: {self.date}"

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    website_url = db.Column(db.String(200), nullable=False, unique=True)
    web_icon_url = db.Column(db.String(400), nullable=True)
    date_completed = db.Column(db.DateTime, default=datetime.utcnow)
    technology_used = db.Column(db.String(100), nullable=True)
    client_name = db.Column(db.String(30), nullable=True)
    source = db.Column(db.String(50), nullable=True)
    tags = db.Column(db.String(50), nullable=True)


    def __repr__(self):
        return f"url: {self.website_url}, client: {self.client_name}, source: {self.source}"


class OtherPortfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    work_type = db.Column(db.String(50), nullable=False, unique=False)


    def __repr__(self):
        return f"{self.name}, type: {self.work_type}"


