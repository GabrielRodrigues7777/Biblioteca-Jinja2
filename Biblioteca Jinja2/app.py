import dados
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

biblioteca = dados.carregar_do_arquivo()


# Rota da página inicial (HTML)
@app.route('/')
def index():
    biblioteca_atual = dados.carregar_do_arquivo()
    return render_template('index.html', livros=biblioteca_atual)


# Rota que retorna todos os livros em JSON
@app.route('/biblioteca', methods=['GET'])
def exibir_json():
    return jsonify(biblioteca), 200


# Rota para inserir um novo livro
@app.route('/biblioteca/insert', methods=['POST'])
def inserir_livro():
    novo_livro = request.get_json()
    biblioteca.append(novo_livro)
    dados.salvar_no_arquivo(biblioteca)
    return jsonify('Novo livro inserido'), 201


# Rota para buscar um livro pelo ISBN
@app.route('/biblioteca/<isbn>')
def achar_isbn(isbn):
    for livro in biblioteca:
        if livro['isbn'] == isbn:
            return jsonify(livro)
    return jsonify('Livro não encontrado'), 404


# Rota para deletar um livro pelo ISBN
@app.route('/biblioteca/delete/<isbn>', methods=['DELETE'])
def deletar_livro(isbn):
    for livro in biblioteca:
        if livro['isbn'] == isbn:
            biblioteca.remove(livro)
            dados.salvar_no_arquivo(biblioteca)
            return jsonify('Livro deletado com sucesso')
    return jsonify('Livro não encontrado'), 404


if __name__ == "__main__":
    app.run(debug=True)
