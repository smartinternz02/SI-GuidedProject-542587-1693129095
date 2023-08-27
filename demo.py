from flask import Flask, url_for,redirect


app=Flask(__name__)

@app.route("/")
def hi():
 return "welcome to fdp program"

@app.route("/faculty")
def faculty():
 return "welcome to all faculty fdp class"

@app.route("/to/<person>")
def to(person):
  if person =="faculty":
   return redirect(url_for("faculty"))
  else:
   return redirect(url_for("desg",desg = person)) 
  
@app.route("/type/<desg>")
def desg(desg):
 return "welcome "+desg+" Go to class "

@app.route("/hello")
def hello():
 return "hello world"

if __name__=="__main__":
 app.run(debug=True)
