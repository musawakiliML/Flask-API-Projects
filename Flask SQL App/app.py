from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root1234@localhost:3306/Author_db'

# SQLITE config
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/ 
# <db_name>.db'

db = SQLAlchemy(app)

with app.app_context():
    
    #print(current_app.name)
    class Authors(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(20))
        age = db.Column(db.Integer)
        specialisation = db.Column(db.String(50))
            
        def __init__(self, name, age, specialisation):
            self.name = name
            self.specialisation = specialisation
            self.age = age
            
        def __repr__(self) -> str:
            return f'<Author {self.id}>'
        
    def create(value, Schema):
            schema = Schema
            
            db.session.add(value)
            db.session.commit()
            return 
        
    db.create_all()
    
    class AuthorSchema(SQLAlchemySchema):
        class Meta(SQLAlchemySchema.Meta):
            model = Authors
            sqla_session = db.session
            load_instances = True
            
        id = fields.Number(dump_only=True)
        name = fields.String(required=True)
        age = fields.Number(required=True)
        specialisation = fields.String(required=True)
    
 
 
    # get request
    @app.route('/authors', methods=['GET'])
    def get_authors():
        get_authors = Authors.query.all()
        author_schema = AuthorSchema(many=True)
        authors = author_schema.dump(get_authors)
        return make_response(jsonify({'authors':authors}))

    # Post request
    @app.route('/authors', methods=['POST'])
    def create_author():
        data = request.get_json()
        author_schema = AuthorSchema()
        author = author_schema.load(data)
        #print(type(author))
        result = author_schema.dump(create(author)).data
        #print(type(result))
        #print(db.session)
        return make_response(jsonify({'authors':result}, 200))
    
if __name__ == "__main__":
    app.run(debug=True)