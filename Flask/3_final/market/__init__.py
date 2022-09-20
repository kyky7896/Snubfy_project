from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:12345678@localhost:3306/market'
app.config['SECRET_KEY']="dev"
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER']='market/static/uploads/'
migrate = Migrate(app, db)

# routes와 데이터베이스 구조 정의하는 models 호출
from market.views import main_views, member_views, product_views, recipe_views, cart_views
app.register_blueprint(main_views.bp)
app.register_blueprint(member_views.bp)
app.register_blueprint(product_views.bp)
app.register_blueprint(recipe_views.bp)
app.register_blueprint(cart_views.bp)

if __name__=='__main__':
    app.run(debug=True)


