from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')



def hello_world():
  return render_template('index.html')



@app.route("/Ninjas")
def Ninjas():
    return render_template('Ninjas.html')

@app.route("/data", methods=["POST", "GET"])
def data():
    return render_template("/dojo/new/dojo.html")

app.run(debug=True)
