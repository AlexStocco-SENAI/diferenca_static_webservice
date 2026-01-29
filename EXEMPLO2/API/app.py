from flask import Flask, render_template, request, redirect, jsonify, session, url_for

app = Flask(__name__)
# Chave necessária para criptografar os cookies de sessão
app.secret_key = 'chave_secreta_para_aula_seguranca'

USER_DB = "godofredo"
PASS_DB = "hamster123"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    dados = request.json
    if dados.get('user') == USER_DB and dados.get('pass') == PASS_DB:
        # Criamos a sessão no servidor
        session['logado'] = True
        return jsonify({"status": "ok"}), 200
    return jsonify({"status": "erro"}), 401

@app.route('/sucesso')
def sucesso():
    # VERIFICAÇÃO DE SEGURANÇA:
    # Se o usuário não tiver a sessão ativa, redireciona de volta para o login
    if not session.get('logado'):
        return redirect(url_for('index'))
    return render_template('sucesso.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)