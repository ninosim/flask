from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Rota para página inicial
@app.route('/')
def index():
    return render_template('formulario.html')

# Rota para receber os dados do formulário
@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Obter dados do formulário
        cpf = request.form['cpf']
        valor = request.form['valor']
        app_name = "HELP_RS_KAMIKAZE"
        
        # Aqui entra o processamento os dados (por exemplo, salvar no banco de dados)
        print(f'CPF: {cpf}, Valor: {valor}, Origem: {app_name}')
        
        # Redirecionar para a página inicial após o envio do formulário
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)