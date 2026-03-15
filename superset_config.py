SECRET_KEY = "Qe5/Ivyoa24qXAHo9PPYWRnaZIIR3wkXtszqN1VZ5QxS0irFDqQ9DZ6P"
# Autoriser SQLite comme source de données (usage local uniquement)
ALLOWED_SQLALCHEMY_DATABASE_URIS = ['sqlite://', 'sqlite:///uber.db']
PREVENT_UNSAFE_DB_CONNECTIONS = False