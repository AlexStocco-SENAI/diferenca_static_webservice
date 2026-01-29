from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login_tradicional():
    erro = None
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        
        if usuario == "godofredo" and senha == "amogirassol":
            return render_template('sucesso.html')
        else:
            erro = "Acesso Negado: Credenciais Incorretas."
            
    return render_template('login.html', erro=erro)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)