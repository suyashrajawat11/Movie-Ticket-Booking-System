import os
from app import create_app, db

# Use production config in production environment
config_name = os.environ.get('FLASK_ENV', 'development')
if config_name == 'production':
    config_name = 'production'
else:
    config_name = 'development'

app = create_app(config_name)

# Initialize database tables
with app.app_context():
    try:
        db.create_all()
        print("✅ Database tables created successfully!")
    except Exception as e:
        print(f"⚠️ Database initialization error: {e}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    debug = config_name == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
