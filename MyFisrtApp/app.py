from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
import csv
import io

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session and flash

# Dummy users
USERS = {'admin': 'pass123'}

# In-memory storage for customers
customers = []
next_id = 1


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if uname in USERS and USERS[uname] == pwd:
            session['user'] = uname
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))


@app.route('/home')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', customers=customers)


@app.route('/add', methods=['POST'])
def add():
    global next_id
    if 'user' not in session:
        return redirect(url_for('login'))

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    customers.append({'id': next_id, 'name': name, 'email': email, 'phone': phone})
    next_id += 1
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    if 'user' not in session:
        return redirect(url_for('login'))

    global customers
    customers = [c for c in customers if c['id'] != id]
    return redirect(url_for('index'))


@app.route('/search')
def search():
    if 'user' not in session:
        return redirect(url_for('login'))

    search_id = request.args.get('id')
    try:
        found = [c for c in customers if str(c['id']) == search_id]
    except ValueError:
        found = []
    return render_template('index.html', customers=found)


@app.route('/export')
def export():
    if 'user' not in session:
        return redirect(url_for('login'))

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Name', 'Email', 'Phone'])
    for c in customers:
        writer.writerow([c['id'], c['name'], c['email'], c['phone']])
    output.seek(0)

    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name='customers.csv'
    )


if __name__ == '__main__':
    app.run(debug=True)
