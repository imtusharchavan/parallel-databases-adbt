from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("PGUSER")}:{os.getenv("PGPASSWORD")}@localhost/{os.getenv("PGDATABASE")}'
# app.debug = True
db = SQLAlchemy(app)


class Seats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    vacancies = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Vacancy %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        category_name = request.form['category']
        available_seats = request.form['available']
        add_seats = Seats(category=category_name, vacancies=available_seats)

        try:
            db.session.add(add_seats)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding more seats"
    
    else:
        seats = Seats.query.order_by(Seats.date_created).all()
        return render_template('index.html', seats=seats)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    seat = Seats.query.get_or_404(id)

    if request.method == 'POST':
        seat.vacancies = request.form['available']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating vacancies'

    else:
        return render_template('update.html', seat=seat)


if __name__ == "__main__":
    app.run(debug=True)