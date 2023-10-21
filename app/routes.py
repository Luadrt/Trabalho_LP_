from flask import Flask, render_template, request, redirect, url_for, session

from flask_mysqldb import MySQL

import MySQLdb.cursors

import re


app = Flask(__name__)



app.secret_key = 'segurança_e_top'


app.config['MYSQL_HOST'] = 'localhost'

app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_PASSWORD'] = 'your password'

app.config['MYSQL_DB'] = 'login'


mysql = MySQL(app)


@app.route('/')


@app.route('/logout')

def logout():

    session.pop('loggedin', None)

    session.pop('id', None)

    session.pop('username', None)

    return redirect(url_for('/register'))


@app.route('/register', methods =['GET', 'POST'])

def register():

    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :

        name = request.form['username']

        password = request.form['password']

        email = request.form['email']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))

        account = cursor.fetchone()

        if account:

            msg = 'Conta já existe!'

        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):

            msg = 'Endereço de email inválido!'

        elif not re.match(r'[a-Za-Zçáãóõôéêíûú]', username):

            msg = 'Nome com caracteres inválidos!'

        elif not username or not password or not email:

            msg = 'Preencha todos os campos do formulário!'

        else:

            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))

            mysql.connection.commit()

            msg = 'Registrado!'

            return redirect('/login')

    elif request.method == 'POST':

        msg = 'Por favor, preencha o formulário'

    return render_template('register.html', msg = msg)

def go_login():
	if login_button == True:
		return redirect('/login')