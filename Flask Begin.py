
from flask import Flask, render_template
app = Flask(__name__)

#basic page
@app.route('/')
def index():
    return 'Reza Putra Pratama'

#page lainnya
@app.route('/reza')
def tes():
    return '<i><h1>Adinda</h1> <h2>Febriyana</h2> <h3>Noorsaid</h3></i> '

#page dengan parameter slash nama
@app.route('/profile/<username>')
def profile(username):
    return 'Hayy kamu %s kan?' %username

#page dengan parameter slash integer
@app.route('/NIM/<int:nim>')
def NIM(nim):
    return 'NIM Anda adalah %s' %nim

@app.route('/user/<name>')
def user(name):
    return render_template("profile.html", name=name)




if __name__ == "__main__":
    app.run(debug= False)
