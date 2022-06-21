from flask import Flask, render_template, request, url_for, redirect
from email. mime.text import MIMEText
import smtplib
from email .message import EmailMessage

app = Flask(__name__)
@app.route("/")
def index() :
 return render_template ("index.html")

@app.route("/sendmail/", methods=["POST"])
def sendemail():
 if request.method == "POST":
    name = request.form[ 'name']
    subject = request.form[ "Subject"]
    email = request.form['replyto']
    message = request.form[ "message"]

    your_name = 'Kenethoriga'
    your_email = "origa.ogutu@students.jkuat.ac.ke"
    your_password = ""

    #Logging in to your email account
    server = smtplib.SMIP('smtp.gmail,com', 587)
    server.chlo()
    server.starttls ()
    server.login(your_email, your_password)

    #sender's and receiver's email address
    sender_email = "kenethoriga@live.com"
    receiver_email = "kenethoriga@live.com"
    msg = EmailMessage ()
    msg.set_content("First Name : "+str(name )+"\nEmail : "+str(email)+"\nSubject : "+str(subject)+"\nMessage: "+str(message))
    msg["Subject"] = "New Response on Persanal Hebsite"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    #send the message via or own smtp server
    try:
        #sending an email
        server.send_message(msg)
    except:
        pass
    return redirect("/");