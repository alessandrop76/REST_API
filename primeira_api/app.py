from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>') #definindo a tipagem como INTEIRO <int: > -- por padrão sempre é STRING
def pessoas(id):
    return jsonify({'id':id, 'Nome': 'Alê', 'Profissão' : 'Desenvolvedor'})

'''
@app.route('/soma/<int:valor1>/<int:valor2>/<int:valor3>')
def soma (valor1, valor2, valor3):
    return jsonify({'soma':valor1 + valor2 + valor3})
'''

@app.route('/soma', methods=['POST', 'GET'])
def soma ():
    if request.method == 'POST':
        dados = json.loads(request.data)   #utilizando o JSON para retornar os dados de uma origem json
        total = sum(dados["valores"])
    elif request.method == 'GET':
        total = 10+10
    return jsonify({'soma':total})  #retornando 'total' que fez a soma dos itens do array pelo comando SUM


if __name__ == '__main__':
    app.run(debug=True)