from flask import Flask, render_template, request, redirect, abort, url_for, flash
from flask_bootstrap import Bootstrap
import smtplib
import os

FROM_EMAIL = os.environ.get("FROM_EMAIL")
PASSWORD = os.environ.get("PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/form_entry', methods=['POST'])
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    print(name)
    print(email)
    print(phone)
    print(message)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject: Client from Website\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
                    )
    
    return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)
