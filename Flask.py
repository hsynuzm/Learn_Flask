from flask import Flask,render_template

app = Flask(__name__)

@app.route("/") #decorator
def index():
   number = 10, "this number python input"
   number2 = 20
   return render_template("index.html",numbers = number, numbers2 = number2)
@app.route("/index2-dicti") #decorator
def about():
    article = dict()
    article ["title"] = "Learning"
    article ["body"] = "The Python"
    article ["author"] = "Me"
    return render_template("index2.html",article= article)
@app.route("/layout") #decorator
def layout():
    return render_template("layout.html")
if __name__ == "__main__":
    app.run(debug=True)


