from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
 
@app.route("/test")
def test():
    output= request.form.to_dict()
    name=output["name"]

    return render_template("tets.py",name)

if __name__=="__main__":
    app.run(debug=True)