from flask import Flask, render_template, url_for, request, make_response, redirect
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# DB_URI = "mongodb+srv://<username>:<password>@<database-name>.mongodb.net/test?retryWrites=true&w=majority"
# app.config["MONGODB_HOST"] = DB_URI

app.config['MONGODB_SETTINGS'] = {
    "db": "users",
}
db = MongoEngine(app)


@app.route('/')
def home():
    #user = request.cookies.get('uid')
    return render_template("index.html")


@app.route('/track/')
def track():
    return render_template("track.html")


@app.route('/contact-us/')
def contact_us():
    return render_template("contactus.html")


@app.route("/logout/")
def logout():
    resp = make_response(render_template('index.html'))
    resp.set_cookie("uid", '', expires=1)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
