from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def page():
    return render_template("Depan.html")

@app.route('/login', methods =['GET','POST'])
def login():
    if request.method == 'POST':
        return 'Metode Post'
    return render_template("login.html")



#####===Running====#####
if __name__ == "__main__":
    app.run(debug=True)