from flask import Flask, render_template, redirect, request, jsonify
from api_consume import piadas

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main_page.html', joke = None, punchline = None)


@app.route("/heavy_joke", methods=['POST'])
def heavy_joke():
    joke, punchline = piadas()
    return render_template('main_page.html', joke=joke, punchline=punchline)
 
    
@app.route("/light_joke", methods=['POST'])
def light_joke():
    setup, delivery = piadas("light_joke")
    return render_template("main_page.html", setup=setup, delivery=delivery)



if __name__ == "__main__":
    app.run(debug=True)

    
