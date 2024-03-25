from flask import Flask, render_template, request, redirect, url_for,send_from_directory
import sqlite3

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
conn.commit()

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['GET','POST'])
def authenticate():
    username = request.form.get('username')
    password = request.form.get('password')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = c.fetchone()

    if user:
        # Redirect to another page if login successful
        return redirect(url_for('another_page'))
    else:
        # Redirect to registration page if user is not found
        return redirect(url_for('register'))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register_user', methods=['GET','POST'])
def register_user():
    username = request.form.get('username')
    password = request.form.get('password')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()

    # Redirect to login page after registration
    return redirect(url_for('login'))

@app.route('/another_page')
def another_page():
    return render_template("index.html")

# @app.route('/custom_html/Users\kisho\OneDrive\Documents\GitHub\AgeWELL-Hackathon:index.html>')
# def custom_html():
#     return send_from_directory(r'C:\Users\kisho\OneDrive\Documents\GitHub\AgeWELL-Hackathon',"index.html")

if __name__ == '__main__':
    app.run(debug=True)
