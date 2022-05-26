from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask('app') 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class lingua(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))

ling = [
  {'name': 'Python'},
  {'name': 'JavaScript'},
  {'name': 'C++'},
  {'name': 'PHP'},
  {'name': 'GoLang'},
  {'name': 'ReactNative'},
]

@app.route('/')
def index():
    lings = lingua.query.all()
    return render_template('index.html',lings=lings, ling=ling)

@app.route('/create', methods=['POST'])
def create():
  name = request.form.get('name')
  ling.append({'name': name})
  new_lings = lingua(name=name)
  db.session.add(new_lings)
  db.session.commit()
  return redirect('/')

if __name__ == '__main__':
  db.create_all()
  app.run(host='0.0.0.0', port=8080)