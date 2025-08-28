from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/no')
def no():
    return "<h1 style='color:red; text-align:center; margin-top:20%; font-size:50px;'>Adiós, me voy a Irapuato 😢</h1>"

@app.route('/si')
def si():
    return render_template('yes.html')

if __name__ == '__main__':
    app.run(debug=True)
