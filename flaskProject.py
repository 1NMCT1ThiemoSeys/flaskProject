from flask import Flask, render_template, redirect, url_for, request
from DbClass import DbClass


app = Flask(__name__)


@app.route('/')
def login():
    error="Welkom"
    return render_template('login.html',error=error)

@app.route('/', methods=['GET', 'POST'])
def login_actie():
    error = None
    if request.method == 'POST':
        naam = request.form['username']
        passwoord = request.form['password']
        db = DbClass()

        if db.login(naam,passwoord)==False :
            error = 'Fout in de gegevens.'
        else:
            return render_template('weerstation.html')
    return render_template('login.html', error=error)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/FAS')
def FAQ():
    return render_template('FAQ.html')

@app.route('/weerstation/<weerstationId>')
def weerstation(weerstationId):
    db = DbClass()
    print(db.getDataFromDatabase(weerstation))

    return render_template('weerstation.html')

if __name__ == '__main__':
    app.run()
