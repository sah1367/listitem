from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
# ایجاد جدول در پایگاه داده اگر وجود ندارد
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM items')
    items = c.fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    if name:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO items (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
