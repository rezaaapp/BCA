from flask import Flask, render_template

app = Flask(__name__)


@app.route('/reza')
def index():
    return 'HALOOO'


@app.route('/')
def page():
    return render_template("Depan.html")


# ##@app.route('/page/reza')
# def user():
#     return render_template("MainPage.html")


#####===Running====#####
if __name__ == "__main__":
    app.run(debug=True)
