# Sharing of content 
# @app.route("/updatefortoday", methods=['GET','POST'])#http://localhost:5000/updatefortoday
# @app.route("/share", methods=['GET'])#http://localhost:5000/share
# @app.route("/clearnotepadtxt", methods=['GET'])#http://localhost:5000/clearnotepadtxt

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Notes %r>' % self.title

# Create the database
with app.app_context():
    db.create_all()

@app.route('/updatefortoday', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:

            new_note = Notes(title=title, content=content)
            db.session.add(new_note)
            db.session.commit()
        return redirect(url_for('share'))
    # For GET request
    return render_template('home.html')

@app.route('/share', methods=["GET"])
def share():
    notes = Notes.query.all()
    return render_template('notes.html', notes=notes)

@app.route('/clearnotepadtxt', methods=['GET'])
def clear():
    db.session.query(Notes).delete()
    db.session.commit()
    return redirect(url_for('share'))

if __name__ == '__main__':
    app.run(debug=True)