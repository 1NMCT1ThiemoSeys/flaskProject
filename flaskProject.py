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
        user = db.login(naam,passwoord)
        if user==False :
            error = 'Fout in de gegevens.'
        else:
            userId = str(user[0][0])
            weerstation(userId)
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

@app.route('/weerstation')
def weerstation(userId):
    db = DbClass()
    weerstation= db.geef_weerstation(userId)
    sensoren = db.geef_sensoren(weerstation[0])
    sensoren = []
    for sensor in sensoren:
        metingen = db.geef_metingen()
    return render_template('weerstation.html',weerstation=weerstation,sensoren=sensoren,metingen=metingen)

if __name__ == '__main__':
    app.run()
