from portfolio_site import create_app
# from portfolio_site.models import OtherPortfolio
# from portfolio_site import db


app = create_app()

if __name__=='__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)