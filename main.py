# API, Application Programming Interface -> Local para disponibilizar recursos e/ou funcionalidades. UMA PONTE
# 1. Objetivo - Criar uma API que diisponibiliza a consulta, criacao, edicao e exclusao
# 2. URL base - localhost
# 3. Endpoints -
# localhost/carros(POST)
# localhost/carros(GET)
# localhost/carros(PUT)
# localhost/carros(DELETE)

from flask import Flask, jsonify, make_response, request
# importa o database
from bd import Carros

# instanciar o módulo flask na nossa variável app
app = Flask('carros')

# primeiro método 1.0 - visualizar dados (GET)
# def get_carros  -> funcao def para retornar a lista de carros
# app.route -> definir que essa função é uma rota para que o flask entenda que aquilo é um método que precisa ser executado
@app.route('/carros', methods=['GET'])
def get_carros():
    return Carros

# primeiro método 1.1 - visualizar dados por id (GET / ID)
@app.route('/carros/<int:id>', methods=['GET'])
def get_carros_id(id):
    for carro in Carros:
        if carro.get('id') == id:
            return jsonify(carro)



# segundo método 2.0 -  criar novos dados (POST)
@app.route('/carros', methods=['POST'])
def criar_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(jsonify(mensagem='Carro cadastrado com sucesso!', carro=carro))

# terceiro método 3.0 - editar dados (PUT)
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_id(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(Carros[indice])
        

# quarto método 4.0 - deletar dados (DELETE)
@app.route('/carros/<int:id>', methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify({'mensagem: ':'Carro excluído com sucesso'})



app.run(port=5000, host='localhost')