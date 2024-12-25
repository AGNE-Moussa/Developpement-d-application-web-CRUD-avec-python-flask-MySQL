from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Mettez votre mot de passe MySQL ici
app.config['MYSQL_DB'] = 'ong_db'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employes")
    employes = cur.fetchall()
    cur.close()
    return render_template('index.html', employes=employes)

@app.route('/ajout', methods=['GET', 'POST'])
def ajout():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        salbase = request.form['salbase']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employes (nom, prenom, salbase) VALUES (%s, %s, %s)", (nom, prenom, salbase))
        mysql.connection.commit()
        return redirect(url_for('index'))
    return render_template('ajout.html')

@app.route('/modif/<int:id>', methods=['GET', 'POST'])
def modif(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        salbase = request.form['salbase']
        cur.execute("UPDATE employes SET nom=%s, prenom=%s, salbase=%s WHERE id=%s", (nom, prenom, salbase, id))
        mysql.connection.commit()
        return redirect(url_for('index'))
    cur.execute("SELECT * FROM employes WHERE id=%s", (id,))
    employe = cur.fetchone()
    cur.close()
    return render_template('modif.html', employe=employe)

@app.route('/sup/<int:id>')
def sup(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employes WHERE id=%s", (id,))
    mysql.connection.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
