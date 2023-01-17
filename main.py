from flask import Flask,render_template
import requests
app = Flask(__name__)

@app.route("/")
def hello_world():
    # names = request.form.get("name")
    # email = request.form.get("email")
    # phone = request.form.get("phone")
    # message = request.form.get("message")
    
    # entry = name=names,emailId =email,Ph_number= phone,message= message
    # db.session.add(entry)
    # db.session.commit()
    return render_template("index.html")

app.run(debug=True)

