from flask import Flask, render_template  

app = Flask(__name__) 

@app.route("/") 
def home(): 
    return render_template('site/page.html')

app.run(host="127.0.0.1", port="1337", debug=True)