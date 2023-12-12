from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from flask import jsonify
from minhas_funcoes import adicionar_valor_arquivo, ler_arquivo, salvar_lista_arquivo
import json
import traceback

app = Flask(__name__)
CORS(app)
# Lista de tarefas como um exemplo de dados
tasks = []


@app.route('/criar', methods=['POST'])
def create_teste():
  nome = request.json['nome']
  email = request.json['email']
  senha = request.json['senha']

  user_data = [{'nome': nome, 'email': email, 'senha': senha}]
  tasks.append(user_data)

  # Adiciona os dados do usuário ao arquivo
  adicionar_valor_arquivo(user_data)

  return {"message": "Usuário criado com sucesso"}, 201


def load_users():
  try:
      with open('mytask.txt', 'r') as file:
          return json.load(file)
  except FileNotFoundError:
      return []


@app.route('/confirmar', methods=['POST'])
def login():
    try:
        login_data = request.get_json()
        email = login_data.get('email')
        senha = login_data.get('senha')

        users_data = load_users()

        for user in users_data:
            if user.get('email') == email and user.get('senha') == senha:
                return jsonify({"message": "Login bem-sucedido"}), 200

        return jsonify({"error": "E-mail ou senha inválidos"}), 401
    except Exception as e:
        print("Erro:", str(e))
        traceback.print_exc()  # Adiciona essa linha para imprimir a exceção completa
        return jsonify({"error": "Erro interno do servidor"}), 500

if __name__ == '__main__':
  app.run(host='0.0.0.0')
