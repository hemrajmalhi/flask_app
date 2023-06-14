from flask import Flask
from flask import url_for
from flask import render_template, request ,redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'email'
app.config['MAIL_PASSWORD'] = 'email_passeword'

mail = Mail(app)

app = Flask(__name__)
app.config['DEBUG'] = True
# url_for('static', filename='style.css')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method=="POST":
        name =request.form['name']
        email =request.form['email']
        message =request.form['message']

        msg = Message('New Contact Form Submission', sender='hemrajmalhi39@gmail.com', recipients=['hemrajmalhi1234@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)
    return render_template("contact.html")






@app.route("/home")
def hello_world():
    return "<p>Hello, World!</p>"





if __name__ == "__main__":
    app.run()

# if __name__ == '__main__':
#     app.run()


