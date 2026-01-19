from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager
from config import Config
from database.db import db
from database.models import User

# Import blueprints
from routes.auth import auth_bp
from routes.proposals import proposals_bp
from routes.pdf import pdf_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database
    db.init_app(app)
    
    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(proposals_bp)
    app.register_blueprint(pdf_bp)
    
    # Home route
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))
    
    # Dashboard route
    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard/index.html')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
