from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'godofredo' and password == 'adoro_girassol':
            return render_template('success.html')
        else:
            return render_template('failure.html')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
