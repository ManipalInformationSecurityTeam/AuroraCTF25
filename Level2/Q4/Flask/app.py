from flask import Flask, request, render_template, make_response
import sqlite3
import os

app = Flask(__name__)

app.static_folder = 'static'

def init_db():
    db_path = 'ctf.db'
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def submit_bid():
    if request.method == 'POST':
        bidder_name = request.form.get('username')
        bid_amount = request.form.get('bid')

        print(f"Received input - Bidder Name: {bidder_name}, Bid Amount: {bid_amount}")

        query = f"SELECT * FROM users WHERE username='{bidder_name}' AND password='{bid_amount}'"
        print(f"Executing SQL query: {query}")

        try:
            conn = sqlite3.connect('ctf.db')
            c = conn.cursor()
            c.execute(query)
            user = c.fetchone()
            conn.close()

            if user:
                response = make_response("<h1>Bid successfully submitted! Access the admin portal for your flag.</h1>")
                if bidder_name.lower() == 'admin':
                    response.set_cookie("is_admin", "true")
                else:
                    response.set_cookie("is_admin", "false")
                return response
            else:
                return "<h1>Bid submission failed! Invalid bidder name or bid amount.</h1>"
        except sqlite3.OperationalError as e:
            print(f"Database Error: {e}")
            return "<h1>Something went wrong. Please try again.</h1>"

    return render_template('login.html')

@app.route('/admin', methods=['GET'])
def admin_portal():
    is_admin = request.cookies.get("is_admin")
    if is_admin == "true":
        return "<h1>Congratulations! Here is your admin flag: actf{02_26_15.7_n_125_03_06.2_3}</h1>"
    else:
        return "<h1>Access Denied. You must be an admin to view this page.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
