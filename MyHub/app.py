from flask import Flask, render_template, request, redirect, flash
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Needed for flashing messages

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    with open('data/projects.json') as f:
        projects = json.load(f)
    return render_template('projects.html', projects=projects)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        print(f"[CONTACT FORM SUBMISSION]")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")

        # Save message to file
        with open("data/messages.txt", "a") as f:
            f.write(f"{name},{email},{message}\n")

        flash("Thank you for your message. I’ll get back to you soon!")
        return redirect('/contact')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)