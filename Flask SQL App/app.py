from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root1234@localhost:3306/Author_db'

# SQLITE config
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/ 
# <db_name>.db'
app.app_context()
db = SQLAlchemy(app)

class Authors (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    specialisation = db.Column(db.String(50))
    
    def __init__(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation
        
    def __repr__(self) -> str:
        return f'<Product {self.id}>'
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
    