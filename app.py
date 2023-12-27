from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+mysqlconnector://sayan:1234@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True) 
    title = db.Column(db.String(200), nullable = False) 
    desc = db.Column(db.String(500), nullable = False) 
    date = db.Column(db.DateTime, default = datetime.utcnow) 

    def __repr__(self) -> str:
        return f'{self.sno} - {self.title}'

@app.route('/')
def index():
    todo = Todo(title = "first", desc = "This is for test")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')
@app.route('/show')
def show():
    alltodo = Todo.query.all()
    print(alltodo)
    return "This is under process"

if __name__ == "__main__":
    app.run(port=8000, debug=True)
    