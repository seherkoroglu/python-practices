from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedule.db'
db = SQLAlchemy(app)

class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(50), nullable=False)

class Constraint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'), nullable=False)
    day = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(10), nullable=False)

# Veritabanı tablolarını oluştur
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    with app.app_context():
        instructors = Instructor.query.all()
        constraints = Constraint.query.all()
    return render_template('index.html', instructors=instructors, constraints=constraints)

@app.route('/add_instructor', methods=['POST'])
def add_instructor():
    with app.app_context():
        name = request.form['name']
        subject = request.form['subject']
        instructor = Instructor(name=name, subject=subject)
        db.session.add(instructor)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_constraint', methods=['POST'])
def add_constraint():
    with app.app_context():
        instructor_id = request.form['instructor_id']
        day = request.form['day']
        time = request.form['time']
        constraint = Constraint(instructor_id=instructor_id, day=day, time=time)
        db.session.add(constraint)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



