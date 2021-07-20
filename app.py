from os import removedirs
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = "verysecretkey"



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bg1")
def bg1():
    return render_template("blog1.html")

@app.route("/peermentor")
def peermentor():
    return render_template("peermentor.html")

@app.route("/ielts")
def ielts():
    return render_template('ielts.html')

@app.route("/studyabroad")
def studyabroad():
    return render_template("studyabroad.html")

@app.route("/leader")
def leader():
    return render_template("leader.html")

@app.route("/businessnpersonal")
def businessnpersonal():
    return render_template("businessnpersonal.html")

@app.route("/choosingcareer")
def choosingcareer():
    return render_template("choosingcareer.html")

@app.route("/foundingbusiness")
def foundingbusiness():
    return render_template("foundingbusiness.html")

@app.route("/findmentor")
def findmentor():
    return render_template("findmentor.html")

@app.route("/becomementor")
def becomementor():
    return render_template("becomementor.html")

@app.route("/request")
def requesthtml():
    return render_template("request.html")

@app.route("/ourmentor")
def ourmentor():
    return render_template("ourmentor.html")

@app.route("/seniorleader")
def seniorleader():
    return render_template("seniorleader.html")

@app.route("/blgs")
def blgs():
    return render_template("Blogs.html")

@app.route("/resourcelibrary")
def resourcelibrary():
    return render_template("resourcelibrary.html")


@app.route("/studyabroad")
def studyabroad():
    return render_template("studyabroad.html")




if __name__ == "__main__":
    app.run(debug=True)

