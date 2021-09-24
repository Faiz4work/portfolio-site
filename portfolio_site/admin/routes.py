from portfolio_site.models import Portfolio
from portfolio_site import admin
from flask_admin.contrib.sqla import ModelView
from portfolio_site.models import Portfolio, EmailLeads
from portfolio_site import db


admin.add_view(ModelView(Portfolio, db.session))
admin.add_view(ModelView(EmailLeads, db.session))