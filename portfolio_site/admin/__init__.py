from flask import Blueprint


myadmin = Blueprint('myadmin', __name__)

from portfolio_site.admin.routes import *