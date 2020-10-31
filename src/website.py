from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    response = render_template('index.html')
    return response

@app.route("/interests")
def interests():
    response = render_template('interests.html')
    return response

@app.route("/aboutme")
def aboutme():
    response = render_template('aboutme.html')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)